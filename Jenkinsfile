podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true)
  ],
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
  ]
  ) {
    node('mypod') {
        stage('Check running containers') {
            container('docker') {
                // example to show you can run docker commands when you mount the socket
                sh 'hostname'
                sh 'docker ps'
            }
        }
        
        stage('Clone repository') {
            container('git') {
                sh 'git clone https://github.com/Andeftd/MasterMG'
            }
        }

        stage('Docker Build') {
            container('docker') {
                dir('MasterMG/dockercoins/worker/') {
                    sh 'docker build -t repository/docker/worker:1.0 .'
                }
            }
        }
    }
}
