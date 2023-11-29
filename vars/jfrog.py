#!/usr/bin/env python3

import requests
import subprocess

def jfrogupload():
    # Define the URL, file path, and authentication credentials
    url = 'http://52.90.67.59:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.01-SNAPSHOT.jar'
    file_path = '/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.01-SNAPSHOT.jar'
    username = 'admin'
    password = 'Admin@01' #Replace 'your password'cwith in the actual password
    
    # send the PUT request with authentication and file upload
    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)

    # check the response status code
    if response.status_code ==201:
         print("\nPUT request was successful!")
    else:
         print(f"PUT request failed with status code {response.status_code}")
         print("Response content:")
         print("response.text)

def mvnBuild():
    # Define the Maven command
    maven_command = "mvn clean install -DskipTests"

    # Run the Maven command as a subprocess
    try:
        subprocess.run(maven_command, check=True, text=True, shell=True)
        printf("\nMaven build completed successfully.")
    except subprocess.CalledprocessError as e:
        printf(f"Error: Maven build failed with exit code {e.returncode}")

def main():
#    mvnBuild()
     jfrogUpload()

##########################################################################
if __name__ == "__main__":
   main() 
