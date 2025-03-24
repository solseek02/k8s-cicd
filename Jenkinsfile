pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_DJANGO_REPO = 'solseek02/mydjango'
        DOCKER_SOLSEEK_REPO = 'solseek02/mysolseek'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Django Image') {
            steps {
                dir('myproject') {
                    script {
                        // Django 이미지 빌드
                        sh "docker build -t ${DOCKER_DJANGO_REPO}:latest ."
                    }
                }
            }
        }
        
        stage('Build Solseek Image') {
            steps {
                dir('mysolseek') {
                    script {
                        // Deepseek 이미지 빌드
                        sh "docker build -t ${DOCKER_SOLSEEK_REPO}:latest ."
                    }
                }
            }
        }
        
        stage('Login to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        
        stage('Push Images') {
            steps {
                script {
                    // Django 이미지 푸시
                    sh "docker push ${DOCKER_DJANGO_REPO}:latest"
                    // Deepseek 이미지 푸시
                    sh "docker push ${DOCKER_SOLSEEK_REPO}:latest"
                }
            }
        }
        
        stage('Deploy to K8s') {
            steps {
                script {
                    // nginx 배포
                    sh 'kubectl apply -f mynginx/k8s-nginx.yaml'
                    // Django 배포
                    sh 'kubectl apply -f myproject/k8s-django.yaml'
                    // Deepseek 배포
                    sh 'kubectl apply -f mysolseek/k8s-deepseek.yaml'
                }
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
        }
    }
}
