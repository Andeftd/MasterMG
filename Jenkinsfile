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
                    sh 'docker build -t worker:1.0 dockercoins/worker/.'
                    sh 'docker tag worker:1.0 anfurtado/dockercoins/worker:1.0'
                    sh 'docker push anfurtado/dockercoins/worker:1.0'
                }
            }
        }
    }
}
