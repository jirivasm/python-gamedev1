This will be a first test to create a python ganme and push it to docker via jenkins installed on casaOS server
- install casaOS with curl -fsSL https://get.casaos.io | sudo bash
- create credentials
- then install jenkins via docker( Docker was installed when I installed CasaOS) with the following command
    docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home jenkins/jenkins 
    this will install docker opening port 8080 and create a volume.
- we need to add the project to jenkins first stem is to add this project to github
- I will need to add a github webhook so jenkins runs the program each time I push the code 
- added ip/8080/github-webhook 
- in order to be able to access github from my jenkins on the server I had to add a tunnel to expose in a safe way my jenkins
- now I can add the webhook and test to see if it runs.