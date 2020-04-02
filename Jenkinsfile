node {
  //checkout scm
  env.each { name, value -> println "Name: $name -> Value $value" }
  stage('Updating Image'){

    sh "printenv"
    echo "The build number is ${env.BUILD_NUMBER}"
    if(env.BRANCH_NAME == "master"){
        echo "hell yeah diry bass"
    }else if(env.BRANCH_NAME == "dev"){
        echo "oh no clean base"
    }

  }


}