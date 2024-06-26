pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Susainathan/First.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('SonarQube Scan') {
            steps {
                 withSonarQubeEnv('MySonar') {
                    sh '''
                    docker run --rm \
                      --network cpo-dev-env-network \
                      -v "$(pwd):/usr/src" \
                      sonarsource/sonar-scanner-cli:latest \
                      sonar-scanner \
                        -Dsonar.projectKey=first \
                        -Dsonar.projectName=First \
                        -Dsonar.sources=src \
                        -Dsonar.host.url=http://172.50.10.5:9000 \
                        -Dsonar.login=sqp_ef3b30ddc87e7e3f82473ad4208624f3bbc881d4
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
