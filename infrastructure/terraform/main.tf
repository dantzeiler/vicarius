provider "aws" {
  region = "us-east-1"
}

#EKS module
module "eks" {
  source                            = "./modules/eks"
  cluster_name                       = var.cluster_name
  cluster_version                   = var.cluster_version
  min_size                          = var.min_size
  max_size                          = var.max_size
  desired_size                      = var.desired_size 
  subnet1                           = var.subnet1
  subnet2                           = var.subnet2
  subnet3                           = var.subnet3
}