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
                      --network sonar_jenkins_network \
                      -v $(pwd):/usr/src \
                      -w /usr/src \
                      sonarsource/sonar-scanner-cli:latest \
                      sonar-scanner \
                        -Dsonar.projectKey=first \
                        -Dsonar.projectName=First \
                        -Dsonar.sources=src \
                        -Dsonar.host.url=http://sonarqube:9000 \
                        -Dsonar.login=your_sonar_token
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
