def call(){
  echo '------excuting Jfrog'
 echo """ curl -X PUT -u admin:Admin@01 -T /home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.01-SNAPSHOT.jar http://44.211.76.218:8082/artifactory/example-repo-local/  
}
