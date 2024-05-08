pipeline {
    agent any

    environment {
        // Define any necessary environment variables here
        // For example, if you need special Docker options, DB settings, etc.
        BUILD_POSTGRESQL = "true"
        BUILD_WAGTAIL = "false"
        BUILD_REACT = "false"
        RUN_TESTS = "false"
        BUILD_MAIN_APP = "false"
        DEPLOY = "false"
    }

    //credentialsBinding {
        // If your Git repository is private, bind credentials here
        // For example, for GitHub:
        // githubToken('GITHUB_TOKEN_CREDENTIAL_ID')
    //}

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']], 
                          userRemoteConfigs: [[url: 'https://github.com/Kishoraditya/tempsaas']],
                          gitTool: 'Git',
                          toolName: 'C:\\Program Files\\Git\\bin\\git.exe'
                          //toolName: 'C:\Program Files\Git\bin\git.exe'
                          //credentialsId: 'YOUR_GITHUB_CREDENTIALS_ID'
                          ]) // Replace with actual ID
            }
        }

        stage('Build PostgreSQL') {
            when {
                expression { return env.BUILD_POSTGRESQL == 'true' } // Add a way to control this stage if needed
            }
            steps {
                dir('tempsaas/tempsaas_postgres') {
                    bat 'docker-compose -p postgres up -d'
                }
            }
        }

        stage('Build Wagtail') {
            when {
                expression { return env.BUILD_WAGTAIL == 'true' } // Conditional execution
            }
            steps {
                dir('tempsaas/tempsaas_wagtail') {
                    bat 'docker-compose -p wagtail up -d'
                }
            }
        }

        stage('Build React') {
            when {
                expression { return env.BUILD_REACT == 'true' } // Conditional execution
            }
            steps {
                dir('tempsaas/tempsaas_react') {
                    bat 'docker-compose -p react up -d'
                }
            }
        }

        stage('Run Tests') {
            when {
                expression { return env.RUN_TESTS == 'true' } // Conditional execution
            }
            steps {
                script {
                    // Sequential or parallel test execution based on your needs
                    dir('tempsaas/tempsaas_wagtail') {
                        bat 'docker-compose -p wagtail run wagtail python manage.py test'
                    }
                    dir('tempsaas/tempsaas_react') {
                        bat 'docker-compose -p react run react npm test'
                    }
                }
            }
        }

        stage('Build Main Application') {
            when {
                expression { return env.BUILD_MAIN_APP == 'true' } // Conditional execution
            }
            steps {
                dir('tempsaas') {
                    bat 'docker build -t my-app .'
                }
            }
        }

        stage('Deploy') {
            when {
                expression { return env.DEPLOY == 'true' } // Conditional execution for deploy stage
            }
            steps {
                // Assuming deployment involves pushing to a registry or similar
                bat 'echo "Deployment steps would go here"'
                // Actual deployment commands
            }
        }
    }
}