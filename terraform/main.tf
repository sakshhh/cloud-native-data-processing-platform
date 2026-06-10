terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

data "aws_ami" "amazon_linux" {

  most_recent = true
  owners = ["amazon"]
  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }
}

resource "aws_key_pair" "devops_key" {
  key_name   = "devops-server-key"
  public_key = file("devops-server-key.pub")
}

resource "aws_security_group" "devops_sg" {

  name        = "devops-security-group"
  description = "Allow SSH access"

  ingress {
    description = "SSH"

    from_port   = 22
    to_port     = 22
    protocol    = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {

    from_port   = 0
    to_port     = 0
    protocol    = "-1"

    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "devops-security-group"
  }
}

resource "aws_instance" "devops_server" {

  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  key_name = aws_key_pair.devops_key.key_name

    vpc_security_group_ids = [
      aws_security_group.devops_sg.id
    ]

  tags = {
    Name = "devops-learning-server"
  }
}
