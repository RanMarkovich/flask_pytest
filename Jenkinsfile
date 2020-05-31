pipeline{
    agent {label 'slave_02'}
    stages{
        stage('install-requirements'){
            steps{
                sh 'pip install -r requirements.txt'
                }
            }
        stage('build-flask-app'){
            steps{
                sh 'docker build -t flask-app .'
                }
            }
        stage('run-flask-app'){
            steps{
                sh 'docker run -d -p 5000:5000 flask-app:latest'
                }
            }
        stage('test-app'){
            steps{
                sh 'pytest test/test_app.py'
            }
        }
    }
}