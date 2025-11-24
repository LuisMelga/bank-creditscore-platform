terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_eks_cluster" "this" {
  name     = "${var.cluster_name}-${var.env}"
  role_arn = "arn:aws:iam::123456789012:role/eks-cluster-role" # TODO: cambiar

  vpc_config {
    subnet_ids = [
      "subnet-aaa111",
      "subnet-bbb222"
    ] # TODO: cambiar a tus subnets
  }
}

output "cluster_name" {
  value = aws_eks_cluster.this.name
}
