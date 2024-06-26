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
                      -v "$WORKSPACE:/usr/src" \
                      --network host \
                      sonarsource/sonar-scanner-cli:latest \
                      sonar-scanner \
                        -Dsonar.projectKey=first \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9001 \
                        -Dsonar.login=sqp_ef3b30ddc87e7e3f82473ad4208624f3bbc881d4 \
                        -Dsonar.python.version=3.x 
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
