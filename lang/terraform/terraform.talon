title: /.*\.tf/
-
document [data] {user.tf_aws_data}: user.browser_open("https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/{tf_aws_data}")
document [resource] {user.tf_aws_resources}: user.browser_open("https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/{tf_aws_resources}")

resource {user.tf_aws_resources}:
    'resource "aws_{tf_aws_resources}" "" {{}}'
    key(left enter up end left:3)
data {user.tf_aws_data}:
    'data "aws_{tf_aws_data}" "" {{}}'
    key(left:4)

item {user.tf_aws_data}: "aws_{tf_aws_data}"
item {user.tf_aws_resources}: "aws_{tf_aws_resources}"
