pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('hello world') {
      steps {
        echo 'hello world!'
      }
    }
    stage('goodbye world') {
      steps {
        echo 'goodbye world!'
      }
    }
  }
}