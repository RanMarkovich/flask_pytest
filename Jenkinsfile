pipeline{
    agent {label 'slave_02'}
    stages{
        stage('install-requirements'){
            steps{
                sh 'pip install -r requirements.txt'
                }
            }
        stage('build'){
            steps{
                sh '/usr/local/bin/docker-compose up -d --build flask-app'
                }
            }
        stage('test-app'){
            steps{
                sh 'pytest test/test_app.py'
            }
        }
    }
}