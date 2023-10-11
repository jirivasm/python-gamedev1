pipeline 
{
  agent any
  stages 
  {
    stage('Build') 
    {
      steps 
      {
        git 'https://github.com/jirivasm/python-gamedev1.git'
        sh "docker build -t jirivasm/game1:${env.BUILD_ID} ."
      }
    }
    stage('push')
    {
      steps
      {
        sh 'echo pushing dockerimage to dockerhub'
        withCredentials([string(credentialsId: 'Dockerhub-pass', variable: 'DockerhPass')]){
            sh "docker login -u jirivasm -p ${DockerhPass}"
         }              
        sh "docker push jirivasm/game1:${env.BUILD_ID}"
      }
    }
  }
}
