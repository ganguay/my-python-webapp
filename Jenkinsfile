pipeline {
    agent any

    environment {
        DOCKER_REGISTRY_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE_TAG = "${DOCKER_REGISTRY_USERNAME}/simple-webapp:${BUILD_NUMBER}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                // Checkout the source code from the repository
                git branch: 'main', url: 'https://github.com/ganguay/my-python-webapp.git'

                // Build the Docker image with Jenkins build number as the tag
                sh "docker build -t ${DOCKER_IMAGE_TAG} ."
                // Log in to Docker Hub
                sh "docker login -u ${DOCKER_REGISTRY_USERNAME} -p ${DOCKER_REGISTRY_PASSWORD}"
                // Push the Docker image to Docker Hub
                sh "docker push ${DOCKER_IMAGE_TAG}"
            }
        }
    }
}
