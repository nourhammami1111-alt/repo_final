pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nourhammami11/simple-flask-app"
        DOCKER_TAG = "latest"
        GIT_REPO = "https://github.com/nourhammami1111-alt/repo_final.git"
        HELM_RELEASE = "flask-app"
        HELM_NAMESPACE = "default"
        HELM_CHART_PATH = "./helm-chart"  // met le chemin de ton chart ici
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

        stage('Deploy with Helm') {
            steps {
                sh """
                helm upgrade --install ${HELM_RELEASE} ${HELM_CHART_PATH} \
                --namespace ${HELM_NAMESPACE} \
                --set image.repository=${DOCKER_IMAGE} \
                --set image.tag=${DOCKER_TAG} \
                --set service.port=5000
                """
            }
        }
    }
