pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git 'https://github.com/danielshine1/WOG.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t wog .'
            }
        }

        stage('Run') {
            steps {
                // Run the Docker container
                sh 'docker run -d -p 8777:8777 -v Scores.txt:/Scores.txt wog'
            }
        }

        stage('Test') {
            steps {
                // Run tests with e2e.py
                sh 'python e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                // Stop and remove the Docker container
                sh 'docker stop $(docker ps -q --filter ancestor=wog)'
                sh 'docker rm $(docker ps -q --filter ancestor=wog)'

                // Push the Docker image to DockerHub
                sh 'docker push danielshine/wog:latest'
            }
        }
    }
}
