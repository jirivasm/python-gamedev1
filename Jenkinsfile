pipeline {
  agent{
    dockerfile true
  }
  stages {
    stage('Build') {
      steps {
        git 'https://github.com/jirivasm/python-gamedev1.git'
        sh 'docker --version'
      }
    }
}
}
