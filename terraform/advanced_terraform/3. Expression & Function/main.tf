variable "pucci" {
  default = "pucci"
}

output "function_startswith1" {
  value = startswith(var.pucci, "pucci")
}

output "function_startswith2" {
  value = startswith(var.pucci, "puccii")
}

output "function_file" {
  value = file("main.tf")
}