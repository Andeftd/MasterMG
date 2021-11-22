podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true)
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
                    sh 'docker tag hasher:1.0 anfurtado/dockercoins:hasher:1.0'
                    sh 'docker tag rng:1.0 anfurtado/dockercoins:rng:1.0'
                    sh 'docker tag webui:1.0 anfurtado/dockercoins:webui:1.0'
                    sh 'docker tag worker:1.0 anfurtado/dockercoins:worker:1.0'
                }
            }
        }
        stage('Docker Push') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker push anfurtado/dockercoins:hasher:1.0'
                    sh 'docker push anfurtado/dockercoins:rng:1.0'
                    sh 'docker push anfurtado/dockercoins:webui:1.0'
                    sh 'docker push anfurtado/dockercoins:worker:1.0'
                }
            }
        }
    }
}
