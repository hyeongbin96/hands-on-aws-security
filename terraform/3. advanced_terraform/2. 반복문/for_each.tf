variable "users" {
#   type = object({
#     hb        = string
#     terraform = string
#     aws       = string
#   })

  type = map(string) 
  default = {
    "hb"        = "/good/"
    "terraform" = "/bad/"
    "hb"        = "/hmm/"
  }
}

resource "aws_iam_user" "this" {
  for_each = var.users
  name     = each.key
  path     = each.value
}

output "test" {
  # value = aws_iam_user.this
  # value = { for k, v in aws_iam_user.this : k => v.arn }
  value = [for _, v in aws_iam_user.this : v.arn]
}