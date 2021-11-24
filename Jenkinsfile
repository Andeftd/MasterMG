podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:latest', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'python', image: 'python:latest', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'maven', image: 'maven:latest', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'sonarqube', image: 'sonarqube:latest', ttyEnabled: true, command: 'cat')
  ],
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
  ]
  ) {
    node('mypod') { 
        stage('Login DockerHub') {
            container('docker') {
                sh 'docker login -u anfurtado -p @e1fG9e93'
            }
        }
        stage('Clone repository') {
            container('git') {
                sh 'git clone https://github.com/Andeftd/MasterMG'
            }
        }
        stage('Test') {
            container('git') {
                sh 'echo "A FAIRE"'
            }
        }
        stage('Analyse') {
            container('sonarqube') {
                sh 'echo "A FAIRE"'
            }
        }
        stage('Maven Build') {
            container('maven') {
                sh 'mvn --version'
                sh 'mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false'
                sh 'mvn package -f my-app/'
                sh 'java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App'
            }
        }
        stage('Docker Build') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker build -t hasher:1.0 dockercoins/hasher/.'
                    sh 'docker build -t rng:1.0 dockercoins/rng/.'
                    sh 'docker build -t webui:1.0 dockercoins/webui/.'
                    sh 'docker build -t worker:1.0 dockercoins/worker/.'
                }
            }
        }
        stage('Docker Tag') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker tag hasher:1.0 anfurtado/hasher:1.0'
                    sh 'docker tag rng:1.0 anfurtado/rng:1.0'
                    sh 'docker tag webui:1.0 anfurtado/webui:1.0'
                    sh 'docker tag worker:1.0 anfurtado/worker:1.0'
                }
            }
        }
        stage('Docker Push') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker push anfurtado/hasher:1.0'
                    sh 'docker push anfurtado/rng:1.0'
                    sh 'docker push anfurtado/webui:1.0'
                    sh 'docker push anfurtado/worker:1.0'
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
/*            options {
                timeout(time: 1, unit: 'MINUTES')
            }*/
            script {
                Exception caughtException = null              
                catchError(buildResult: 'SUCCESS', stageResult: 'ABORTED') {
                    try {
                        container('python') {
                            sh 'pip --version'
                            sh 'pip3 install locust'
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
