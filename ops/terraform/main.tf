provider "aws" {
  region = "your_aws_region"
}

resource "aws_instance" "flask_instance" {
  ami           = "your_ami_id"
  instance_type = "t2.micro"
  key_name      = "your_key_pair_name"  # Make sure to replace with your key pair name

  tags = {
    Name = "FlaskAppInstance"
  }

  // Add any additional configuration like subnet_id, security_group_id, etc., as needed
}

resource "aws_security_group" "flask_sg" {
  name        = "flask_sg"
  description = "Security group for Flask app"

  ingress {
    from_port   = 5000  // Port for Flask app
    to_port     = 5000  // Port for Flask app
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  // Allowing traffic from any IP address for demo purposes, restrict as needed
  }

  // Add any additional ingress or egress rules as needed
}

output "public_ip" {
  value = aws_instance.flask_instance.public_ip
}
