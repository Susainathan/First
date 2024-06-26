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
                withSonarQubeEnv('sonar-scanner') {
                    sh """
                    sonar-scanner \
                        -Dsonar.projectKey=your_project_key \
                        -Dsonar.projectName="Your Project Name" \
                        -Dsonar.sources=src \
                        -Dsonar.language=py \
                        -Dsonar.sourceEncoding=UTF-8
                    """
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
