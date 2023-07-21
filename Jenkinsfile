pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                // Checkout the source code from the repository
                git branch: 'main', url: 'https://github.com/ganguay/my-python-webapp.git'

                // Build the Docker image with Jenkins build number as the tag
                sh "docker build -t your-docker-registry/simple-webapp:${BUILD_NUMBER} ."
                // Push the Docker image to your Docker registry
                sh "docker push your-docker-registry/simple-webapp:${BUILD_NUMBER}"
            }
        }
    }
}
