pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "simple-flask-app"
        DOCKER_TAG = "latest"
        GIT_REPO = "https://github.com/nourhammami1111-alt/repo_final.git"
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

        stage('Run Docker container') {
            steps {
                // Arrêter et supprimer l'ancien container si existant
                sh "docker stop ${DOCKER_IMAGE} || true"
                sh "docker rm ${DOCKER_IMAGE} || true"
               
                // Lancer le nouveau container
                sh "docker run -d --name ${DOCKER_IMAGE} -p 5000:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }
    }

    post {
        success {
            echo "Pipeline terminé avec succès !"
        }
        failure {
            echo "Pipeline échoué"
        }
    }
}
