podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'kubectl', image: 'bitnami/kubectl', ttyEnabled: true, command: 'cat')
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
        stage('Build k8s objects on minikube') {
            container('kubectl') {
                dir('MasterMG/') {
                    /*sh 'kubectl apply -f dockercoins/hasher/.'
                    sh 'kubectl apply -f dockercoins/rng/.'
                    sh 'kubectl apply -f dockercoins/webui/.'
                    sh 'kubectl apply -f dockercoins/worker/.'*/
                    sh 'kubectl get po -n jenkins'
                }
            }
        }
    }
}
