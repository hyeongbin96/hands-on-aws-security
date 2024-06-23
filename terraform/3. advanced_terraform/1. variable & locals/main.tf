# variable
variable "var" {
  type    = string
  default = "variable example"
}

variable "tfvars" {
  type    = string
}

output "this" {
  value = var.var
}

output "this1" {
  value = var.tfvars
}

# variable "dynamic-var" {
#   #default = var.var # "variable example"
# }

# locals
locals {
  tf = var.var
}

output "locals-test" {
  value = local.tf
}