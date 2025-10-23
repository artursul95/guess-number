pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/artursul95/guess-number.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('artursul95/guessnum:latest')
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-login') {
                        docker.image('artursul95/guessnum:latest').push()
                    }
                }
            }
        }
    }
}