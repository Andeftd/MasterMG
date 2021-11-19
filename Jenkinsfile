podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true)
  ],
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
  ]
  ) {
    node('mypod') { 
        stage('Clone repository') {
            container('git') {
                sh 'git clone https://github.com/Andeftd/MasterMG'
            }
        }

        stage('Docker Build') {
            container('docker') {
                dir('MasterMG/') {
                    sh 'docker build -t worker:1.0 dockercoins/worker/.'
                    sh 'docker tag worker:1.0 192.168.49.2:32002/repository/docker/worker:1.0'
                    sh 'docker push 192.168.49.2:32002/repository/docker/worker:1.0'
                }
            }
        }
    }
}
