pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                sh 'pip3 install --break-system-packages -r requirements.txt'

            }

        }

    }

}