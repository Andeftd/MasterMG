podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true)
  ],
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
  ]
  ) {
    node('mypod') { 
        stage('Preparation Docker') {
            container('docker') {
                sh 'mkdir /etc/docker && echo "{ "insecure-registries":["192.168.49.2:32001"] }" >> /etc/docker/daemon.json'
                sh 'mkdir /etc/default && echo "DOCKER_OPTS="--config-file=/etc/docker/daemon.json"" >> /etc/default/docker'
                sh 'systemctl stop docker && systemctl start docker'
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
                    sh 'docker tag worker:1.0 192.168.49.2:32001/repository/docker/worker:1.0'
                    sh 'docker push 192.168.49.2:32001/repository/docker/worker:1.0'
                }
            }
        }
    }
}
