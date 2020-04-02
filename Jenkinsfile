node {
  //checkout scm
  env.each { name, value -> println "Name: $name -> Value $value" }
  stage('Updating Image'){

    sh "printenv"
    echo "The build number is ${env.BUILD_NUMBER}"
  }

  stage('Deliver for development') {
    when {
        branch 'dev'
    }
    steps {
        echo "Dev branch"
    }
  }
  stage('Deploy for production') {
      when {
          branch 'master'
      }
      steps {
          echo "Master branch"
      }
  }
}