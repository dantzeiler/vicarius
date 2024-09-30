provider "aws" {
  region = "eu-north-1"
}

#EKS module
module "eks" {
  source                            = "./modules/eks"
  cluster_name                      = var.cluster_name
  cluster_version                   = var.cluster_version
  min_size                          = var.min_size
  max_size                          = var.max_size
  desired_size                      = var.desired_size 
}

#ECR module
module "ecr" {
  source                            = "./modules/ecr"
  ecr_python_name                   = var.ecr_python_name
}