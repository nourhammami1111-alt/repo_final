pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nourhammami11/simple-flask-app"
        DOCKER_TAG = "latest"
        GIT_REPO = "https://github.com/nourhammami1111-alt/repo_final.git"
        HELM_RELEASE = "flask-app"
        HELM_CHART_PATH = "./helm-chart" // chemin vers ton Helm chart
        HELM_NAMESPACE = "default"
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: "${GIT_REPO}"
            }
        }

        stage('Build Docker image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                                  usernameVariable: 'USERNAME',
                                                  passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }
            }
        }

        stage('Push Docker image') {
            steps {
                sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }

        stage('Run Docker container locally') {
            steps {
                // nom de conteneur valide sans slash
                sh "docker stop flask-app || true"
                sh "docker rm flask-app || true"
                sh "docker run -d --name flask-app -p 5000:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
