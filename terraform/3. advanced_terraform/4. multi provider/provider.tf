provider "aws" {
  region = "ap-northeast-2"
}

provider "aws" {
  alias = "apne3"
  region = "ap-northeast-3"
}