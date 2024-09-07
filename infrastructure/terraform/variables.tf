# Variables
variable "environment" {
  type = string
}

variable "cluster_name" {
  type = string
}

variable "cluster_version" {
  type        = string
  description = "version of the EKS cluster. example 1.29"
}

variable "min_size" {
  type        = number
  description = "version of the EKS cluster. example 1.29"
}

variable "max_size" {
  type        = number
  description = "version of the EKS cluster. example 1.29"
}

variable "desired_size" {
  type        = number
  description = "version of the EKS cluster. example 1.29"
}