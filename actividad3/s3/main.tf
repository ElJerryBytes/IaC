terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "gerardo_bucket_terr" {
  bucket = "gerardo-bucket-terraform"
  tags = {
    Name = "GerardoBucketTerraform"
  }
}

# Output para mostrar el nombre del bucket
output "bucket_name" {
  value = aws_s3_bucket.gerardo_bucket_terr.bucket
}
