pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nourhammami11/simple-flask-app"
        DOCKER_TAG = "latest"
        GIT_REPO = "https://github.com/nourhammami1111-alt/repo_final.git"
        HELM_RELEASE = "simple-flask-app"
        HELM_CHART_DIR = "./simple-flask-app"
        K8S_NAMESPACE = "default"
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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                }
            }
        }

        stage('Push Docker image') {
            steps {
                sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }

        stage('Deploy to Kubernetes with Helm') {
            steps {
                sh """
                    helm upgrade --install ${HELM_RELEASE} ${HELM_CHART_DIR} \
                        --namespace ${K8S_NAMESPACE} \
                        --set image.repository=${DOCKER_IMAGE} \
                        --set image.tag=${DOCKER_TAG} \
                        --set service.port=5000 \
                        --wait
                """
            }
        }

        stage('Run Docker container locally (optional)') {
