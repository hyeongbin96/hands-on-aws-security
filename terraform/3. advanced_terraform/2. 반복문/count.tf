variable "user" {
  type      = list(string)
  default   = ["hb", "terraform", "aws"]
}

resource "aws_iam_user" "this" {
  count = length(var.user)
  name = var.user[count.index]
}