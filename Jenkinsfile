pipeline {
  agent{
    dockerfile true
  }
  stages {
    stage('Build') {
      steps {
        git 'https://github.com/jirivasm/python-gamedev1.git'
        sh 'docker --version'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
}
}
