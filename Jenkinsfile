node {
  //checkout scm
  env.each { name, value -> println "Name: $name -> Value $value" }
  stage('Updating Image'){

    sh "printenv"
    echo "The build number is ${env.BUILD_NUMBER}"
  }
}