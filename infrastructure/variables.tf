variable "domain" {
  default = "nhsd-hackday2018-mh"
}

variable "aws_region" {
  default = "eu-west-2"
}

variable "safe_ip_addresses" {
  type = "list"
  default = [
    "62.253.231.2",
    "194.176.0.0/16"
  ]
}

variable "aws_profile" {
  default = "mcbh"
}
