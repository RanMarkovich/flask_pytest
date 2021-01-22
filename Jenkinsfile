pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'docker build app -t flask_app:latest'
        sh 'docker run --name flask_app -d -p 5000:5000 flask_app:latest'
      }
    }
    stage('test') {
      steps {
        sh 'pytest pytest app/tests'
      }
    }
    stage('tear down') {
      steps {
        sh 'docker rm -f flask_app'
      }
    }
  }
}