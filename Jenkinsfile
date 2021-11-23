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
                /*withKubeConfig([credentialsId: 'c023c659-ab51-4d75-ac2e-b360d639fbbf', 
                                caCertificate: '-----BEGIN CERTIFICATE-----\nMIIDBjCCAe6gAwIBAgIBATANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwptaW5p\na3ViZUNBMB4XDTIxMTExNjE0NTgwNloXDTMxMTExNTE0NTgwNlowFTETMBEGA1UE\nAxMKbWluaWt1YmVDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMZj\n5Al7IhFvKe3Fugyx/An3lEqfiti807rzoomQtdR52kWhLlzJi7ExiQiW98KXGTnk\nLZVHhNAWa5K0ie/IWJD2QrrvLi2FoqGW4gtqkmukI6MDbPIsnOcbScWL6fHNgBLu\nbFX47hbyl6tohFp7Fw1Fp+z6rE2TULJUznvnrmeQXp286Ge22wHWGVwrDX4fAyKE\nmPZwgVxjNRh5Dxf8nfuOfqFFtv5/GFSjvLisf+k0G9C0Z4utaMjBnKNY2Ok8vPCc\nISF+fjKNINzZRgYHYk9y7o4lJ/NU+hpqNSo8Hb0JcDRNIs7tQWfA2nlFAVucdrWh\nE9E9te/18PrhjnxQRmkCAwEAAaNhMF8wDgYDVR0PAQH/BAQDAgKkMB0GA1UdJQQW\nMBQGCCsGAQUFBwMCBggrBgEFBQcDATAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQW\nBBTh1wZj6Uk4RYLOo3IbAUG0u/5DlDANBgkqhkiG9w0BAQsFAAOCAQEAmLYWeCtR\nZEBK2lTDMGNhX8Sa7PpOCUxzKkrpR0820+zNfk/8ndrU46BAMCxkShxuMSJJje2T\neBPjqHiSw3uTJ4xf0+woZTCfR19ZSER703M1/pn/+phvs+h0ZWcKjERoQ+XcZk7b\nC+B4fkkJzQlu5gBJ06b+c2aP/f9N0qrdThlU7Sdt/L0fSMyB4K3zL1tXizvc6a2W\nwNeJ9qXJ35w4xCcdoZafmUFzt9kStWRZm5gW/giWep37jPfHpbLe0Mw90nJe8Bh/\nyqcLWjFrkaJIXQstWGMsTULUBVjiY2baWKn/kMnEhWAaeuc8tfD9nNiha7TljvL0\nK57+Sw4AE9WzRg==\n-----END CERTIFICATE-----\n',
                                serverUrl: 'https://192.168.49.2:8443',
                                contextName: 'minikube',
                                clusterName: 'minikube',
                                namespace: 'default'
                                ]) {
                    sh 'kubectl apply -f MasterMG/dockercoins/hasher/.'
                    sh 'kubectl apply -f MasterMG/dockercoins/rng/.'
                    sh 'kubectl apply -f MasterMG/dockercoins/webui/.'
                    sh 'kubectl apply -f MasterMG/dockercoins/worker/.'*/
                sh 'sudo kubectl get ns'
                  
                
            }
        }
    }
}
