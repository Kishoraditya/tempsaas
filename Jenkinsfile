pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build PostgreSQL') {
            steps {
                // Build and run the PostgreSQL database
                dir('tempsaas/tempsaas_postgres') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Build Wagtail') {
            steps {
                // Build and run the Wagtail application
                dir('tempsaas/tempsaas_wagtail') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Build React') {
            steps {
                // Build and run the React application
                dir('tempsaas/tempsaas_react') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests for the Wagtail and React applications
                dir('tempsaas/tempsaas_wagtail') {
                    sh 'docker-compose run wagtail python manage.py test'
                }
                dir('tempsaas/tempsaas_react') {
                    sh 'docker-compose run react npm test'
                }
            }
        }

        stage('Build Main Application') {
            steps {
                // Build the main application image
                dir('tempsaas') {
                    sh 'docker build -t my-app .'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application to a production environment
                // You may need to add additional steps here, such as pushing the
                // application image to a registry, or using a deployment tool
                // to update the production environment
                sh 'docker-compose up -d'
            }
        }
    }
}