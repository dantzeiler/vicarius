# Variables

variable "cluster_name" {
  type = string
}

variable "cluster_version" {
  type        = string
  description = "cluster_version"
}

variable "min_size" {
  type        = number
  description = "min_size"
}

variable "max_size" {
  type        = number
  description = "max_size"
}

variable "desired_size" {
  type        = number
  description = "desired_size"
}