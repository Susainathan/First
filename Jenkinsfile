pipeline {
    agent any
    environment {
        SONARQUBE_SERVER = 'MySonar'
        SONARQUBE_TOKEN = credentials('sqp_ef3b30ddc87e7e3f82473ad4208624f3bbc881d4')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Susainathan/First.git'
            }
        }
        // stage('SonarQube Scan') {
        //     steps {
        //         withSonarQubeEnv(SONARQUBE_SERVER) {
        //             sh '''
        //             docker run --rm \
        //               -v "$WORKSPACE:/usr/src" \
        //               --network host \
        //               sonarsource/sonar-scanner-cli:latest \
        //               sonar-scanner \
        //                 -Dsonar.projectKey=first \
        //                 -Dsonar.sources=. \
        //                 -Dsonar.host.url=http://localhost:9001 \
        //                 -Dsonar.login=${SONARQUBE_TOKEN} \
        //                 -Dsonar.python.version=3.x \
        //                 -Dsonar.scm.provider=git
        //             '''
        //         }
        //     }
        // }
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
