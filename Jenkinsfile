pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git 'https://github.com/jirivasm/python-gamedev1.git'
        sh 'docker build -t jirivasm/tictactoe:@{env.BUILD_ID}'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
}
}
