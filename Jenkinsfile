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
                    docker.build('artursul95/guess-number:latest')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-login') {
                        docker.image('artursul95/guess-number:latest').push()
                    }
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                script {

                    sh 'kubectl delete pod myapp-pod --ignore-not-found=true'
                    sh 'kubectl apply -f myapp.yaml'
                    sh 'kubectl get pods'
                }
            }
        }
    }
}