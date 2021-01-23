pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
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