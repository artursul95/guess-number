pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'artursul95/guess-number-game'
        DOCKER_TAG = "${env.BUILD_ID}"
    }

    stages {
        stage('Check Python') {
            steps {
                sh '''
                    python --version
                    pip --version
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "Checking files..."
                    ls -la

                    if [ -f "main.py" ]; then
                        echo "✅ main.py found"
                        # Простой тест
                        python -c "print('Python is working!')"
                    else
                        echo "❌ main.py not found!"
                        exit 1
                    fi
                '''
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-creds') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push('latest')
                    }
                }
            }
        }
        stage('Cleanup') {
            steps {
                sh '''
                    # Удалить старые образы
                    docker system prune -f --filter "until=24h"
                    # Удалить dangling images
                    docker image prune -f
                '''
            }
        }
    }
}