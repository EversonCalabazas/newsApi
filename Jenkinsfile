pipeline{
    agent any
    stages{
        stage('version'){
            steps{
                sh 'python --version'
            }
        }
        stage('app'){
            steps{
                sh 'python app.py'
            }
        }
    }
}
