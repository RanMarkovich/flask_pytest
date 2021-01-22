pipeline {
  agent {
    docker {
      label "docker && linux"
      image "python:3.7"
        }
      }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest tests/test_app.py'
      }
    }
  }
}