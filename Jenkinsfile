pipeline {
  agent { docker { image 'python:3.7.6' } }

    stage('test') {
      steps {
        sh 'python app.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}