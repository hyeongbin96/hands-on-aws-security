# resource "aws_s3_bucket" "apne2" {
#   bucket = "tf-apne2-hb-bk"
# }

# # 오사카 리전
# resource "aws_s3_bucket" "apne3" {
#   bucket = "tf-apne3-hb-bk"
#   provider = aws.apne3
# }

resource "aws_vpc" "apne2" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" = "apne2-vpc"
  }
}

resource "aws_vpc" "apne3" {
  cidr_block = "10.0.0.0/16"
  provider = aws.apne3
  tags = {
    "Name" = "apne3-vpc"
  }
}