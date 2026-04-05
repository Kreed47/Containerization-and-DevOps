# ** Lab-7 : Implementation of CI-CD Pipeline using Jenkins, GitHub and DockerHub ** #

### *** Step - 1 : Create a repository on Github ###
![](Screenshots/Screenshot%202026-04-04%20092100.png)

#### app.py ####
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline!"
    #return "Hello from CI/CD Pipeline!, my sapid is 123456"

app.run(host="0.0.0.0", port=80)

#### requirements.txt ####
flask

#### Dockerfile ####
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "app.py"]

#### Jenkinsfile ####
pipeline {
    agent any

    environment {
        IMAGE_NAME = "your-dockerhub-username/myapp"
    }

    stages {

        stage('Clone Source') {
            steps {
                git 'https://github.com/your-username/my-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
                    sh 'echo $DOCKER_TOKEN | docker login -u your-dockerhub-username --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
    }
}

### Step - 2: Setup Jenkins with Docker ###
pipeline {
    agent any

    environment {
        IMAGE_NAME = "kreed2317/myapp"
    }

    stages {

        stage('Clone Source') {
            steps {
                git 'https://github.com/kreed47/lab-myapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
                    sh 'echo $DOCKER_TOKEN | docker login -u kreed2317 --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
    }
}

![](Screenshots/Screenshot%202026-04-04%20092150.png)

#### Access Jenkins using password ####
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword

### Step - 3: Add Dockerhub Credentials to Jenkins ###
![](Screenshots/Screenshot%202026-04-04%20092233.png)

#### Create Pipeline Job ####

### Step - 4: Install npm to setup tunnel ###
![](Screenshots/Screenshot%202026-04-04%20094310.png)
![](Screenshots/Screenshot%202026-04-04%20094327.png)

### Step - 5 : Push changes to github and watch process ###
![](Screenshots/Screenshot%202026-04-04%20095631.png)