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

                    docker.build('guess-number')
                }
            }
        }

        stage('Run Container (Optional)') {
            steps {
                script {
                    sh 'docker run --rm guess-number'
                }
            }
        }
    }
}
