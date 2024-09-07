#######################################
######### Create ECR Repo #############
#######################################

resource "aws_ecr_repository" "ecr-python" {
  name                 = var.ecr_python_name
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}