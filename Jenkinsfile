pipeline {

    agent { label 'dockerserver' }

    stages {
        stage('Verify Branch'){
            steps {
                echo "${GIT_BRANCH}"
                }
            }
        stage('Docker Build') {
            steps {
                sh(script: 'docker images -a')
                sh(script: 'docker build -t flask_app .')
            }
        }
    }
}