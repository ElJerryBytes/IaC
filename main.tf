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

resource "aws_instance" "gerardo_server_terr" {
  ami           = "ami-0b016c703b95ecbe4"
  instance_type = "t3.micro"

  tags = {
    Name = "GerardoServerTerraform"
  }
}

output "server_name" {
  value = aws_instance.gerardo_server_terr.tags.Name
}