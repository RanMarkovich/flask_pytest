pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'docker-compose up -d --build flask_app'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest tests/test_app.py'
      }
    }
    stage('tear down') {
      steps {
        sh 'docker rm -f flask_app'
      }
    }
  }
}