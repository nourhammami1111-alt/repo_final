pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nourhammami11/simple-flask-app"
        DOCKER_TAG = "latest"
        GIT_REPO = "https://github.com/nourhammami1111-alt/repo_final.git"
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials' // ID du credential Jenkins
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
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}",
                                                  usernameVariable: 'DOCKER_USER',
                                                  passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker image') {
            steps {
                sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }

        stage('Run Docker container') {
    steps {
        sh "docker stop simple-flask-app || true"
        sh "docker rm simple-flask-app || true"
        sh "docker run -d --name simple-flask-app -p 5000:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
    }
}
    }

    post {
        success {
            echo "Pipeline terminé avec succès ! 🎉"
        }
        failure {
            echo "Pipeline échoué 😢"
        }
    }
}

