podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:latest', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'locust', image: 'locustio/locust', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'maven', image: 'maven:latest', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'python', image: 'python:3.7.12-alpine3.15', ttyEnabled: true, command: 'cat'),
  ],
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
  ]
  ) {
    node('mypod') { 
        stage('Login DockerHub') {
            withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'username', passwordVariable: 'password')]) {
                container('docker') {
                    sh "docker login -u '${username}' -p '${password}'"
                }
            }
        }
        stage('Clone repository') {
            container('git') {
                sh 'git clone https://github.com/Andeftd/MasterMG'
                dir('MasterMG/') {
                    shortCommit = sh(returnStdout: true, script: "git log -n 1 --pretty=format:'%h'").trim()
                    env.commit_var = shortCommit
                }
            }
        }
        stage('Test unitaire') {
            container('python') {
                sh 'pip3 install unittests2 requests nose coverage nose-watch'
                dir('MasterMG/') {
                    sh 'nosetests --with-xunit'
                    validate = sh(returnStdout: true, script: "echo \$?")
                    env.validate_var = validate
                    if (env.validate_var != '0') {
                        currentBuild.result = 'FAILURE'
                        error 'Build failed!'
                    }
                }
            }
        }
        stage('Analyse') {
            def scannerHome = tool 'SonarQube Scanner 4.0';
            withSonarQubeEnv('SonarqubeMasterSG') {
                sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=develop -Dsonar.sources=."
                def qg = waitForQualityGate() // Reuse taskId previously collected by withSonarQubeEnv
                if (qg.status != 'OK') {
                     error "Pipeline aborted due to quality gate failure: ${qg.status}"
                }
            }
        }
        stage('Maven Build') {
            container('maven') {
                sh 'mvn --version'
                sh 'mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false'
                sh 'mvn package -f my-app/'
            }
        }
        stage('Docker Build') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker build -t hasher:latest dockercoins/hasher/.'
                    sh "docker build -t hasher:'${env.commit_var}' dockercoins/hasher/."
                    sh 'docker build -t rng:latest dockercoins/rng/.'
                    sh "docker build -t rng:'${env.commit_var}' dockercoins/rng/."
                    sh 'docker build -t webui:latest dockercoins/webui/.'
                    sh "docker build -t webui:'${env.commit_var}' dockercoins/webui/."
                    sh 'docker build -t worker:latest dockercoins/worker/.'
                    sh "docker build -t worker:'${env.commit_var}' dockercoins/worker/."
                }
            }
        }
        stage('Docker Tag') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker tag hasher:latest anfurtado/hasher:latest'
                    sh "docker tag hasher:'${env.commit_var}' anfurtado/hasher:'${env.commit_var}'"
                    sh 'docker tag rng:latest anfurtado/rng:latest'
                    sh "docker tag rng:'${env.commit_var}' anfurtado/rng:'${env.commit_var}'"
                    sh 'docker tag webui:latest anfurtado/webui:latest'
                    sh "docker tag webui:'${env.commit_var}' anfurtado/webui:'${env.commit_var}'"
                    sh 'docker tag worker:latest anfurtado/worker:latest'
                    sh "docker tag worker:'${env.commit_var}' anfurtado/worker:'${env.commit_var}'"
                }
            }
        }
        stage('Docker Push') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker push anfurtado/hasher:latest'
                    sh "docker push anfurtado/hasher:'${env.commit_var}'"
                    sh 'docker push anfurtado/rng:latest'
                    sh "docker push anfurtado/rng:'${env.commit_var}'"
                    sh 'docker push anfurtado/webui:latest'
                    sh "docker push anfurtado/webui:'${env.commit_var}'"
                    sh 'docker push anfurtado/worker:latest'
                    sh "docker push anfurtado/worker:'${env.commit_var}'"
                }
            }
        }
        stage('Deploy - Staging') {
            container('kubectl') {
                sh "kubectl get pods"
                sh "kubectl create ns dockercoins --dry-run=client -o yaml | kubectl apply -f -"
                sh 'kubectl apply -f MasterMG/dockercoins/hasher/.'
                sh 'kubectl apply -f MasterMG/dockercoins/rng/.'
                sh 'kubectl apply -f MasterMG/dockercoins/webui/.'
                sh 'kubectl apply -f MasterMG/dockercoins/worker/.'
                sh 'kubectl apply -f MasterMG/dockercoins/redis/.'
                /*sh 'kubectl get deployments -o name -n dockercoins | sed -e "s#.*\/##g" | xargs -I {} kubectl patch deployment {} -n dockercoins -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"'*/
            }
        }
        stage('Regression test') {
            container('git') {
                sh 'echo "A FAIRE"'
            }
        }
        stage('Load test') {
            /*options {
                timeout(time: 1, unit: 'MINUTES')
            }*/
            script {
                Exception caughtException = null              
                catchError(buildResult: 'SUCCESS', stageResult: 'ABORTED') {
                    try {
                        container('locust') {
                            sh 'locust -V'
                            sh 'locust -f MasterMG/dockercoins/locust/locustfile.py --host=http://192.168.49.2:32080'
                        } 
                    } catch (org.jenkinsci.plugins.workflow.steps.FlowInterruptedException e) {
                        error "Caught ${e.toString()}"
                    } catch (Throwable e) {
                        caughtException = e
                    }
                }
                if (caughtException) {
                    error caughtException.message
                }
            }
        }
        stage('Deploy - Production') {
            container('kubectl') {
                input "Deploy to production ?"
                sh 'echo "A FAIRE"'
            }
        }
    }
}
