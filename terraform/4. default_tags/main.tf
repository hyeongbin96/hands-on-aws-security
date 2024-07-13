provider "aws" {
  region = "ap-northeast-2"

  default_tags {
    tags = {
      Name = "hb"
      Team = "Cloud"
    }
  }
}

locals {
  tags = {
    Name = "hb"
    Team = "Cloud"
  }
}

resource "aws_iam_user" "this" {
  name = "hb"
  tags = {
    "Date" = "2024-07-13"
  }
}
