# vicarius-Barkuni-corp, Powered by Dan !
Welcome to the Guide 

# building 
to use this application simply clone the repo to your local station. 
any new commits to this repo will automatically trigger the build process which will grab all files unser the application folder and build a new image. 
this new image will be sent to python-application ECR. 

# deploying
To deploy the newlly updated code and image simple run the "Deploy Helm Chart to EKS" github action. 

#infrastrucre information
The AWS EKS wasa fully formed using Terraform. 
The python application is deployed using helm charts. 

# application information 
The python application uses flask for web framwork interface.


# Tools used in this project : 

1. Python - Flask
2. Terraform – Module ( use existing module )
3. Docker
4. Kubernetes manifest/Helm chart

# Bonuses
## ALB 
##The application  include an ALB and can accessed currently by browsing to : 
k8s-default-pythonin-acd2d71822-1416919428.us-east-1.elb.amazonaws.com
## DNS
The site lacks a DNS due to not knowing where the domain is hosted 
## API ROUTE 
the Site Implements an API router that displays all running pods in the "kube-system"
namespace.

This can be access by going to the /pods webpage
## Pipeline in github 
The site is suppoerted by a fully functioning CI\CD process by Implementing a pipeline for updating the code and Docker in GitHub Actions.
instructions on how to use the pipeline can be found at the top. 


