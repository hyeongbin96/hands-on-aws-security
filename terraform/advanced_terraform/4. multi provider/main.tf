resource "aws_s3_bucket" "apne2" {
  bucket = "tf-apne2-hb-bk"
}

# 오사카 리전
resource "aws_s3_bucket" "apne3" {
  bucket = "tf-apne3-hb-bk"
  provider = aws.apne3
}