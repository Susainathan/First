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
                    docker run --rm alpine echo "Hello"
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
