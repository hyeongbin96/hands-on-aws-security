module "iam" {
  source = "./user"
  tf-role = "hyeongbin"
#   path = "/tf"
}

output "user_arn" {
  value = module.iam.arn
}