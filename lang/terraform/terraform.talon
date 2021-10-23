title: /.*\.tf/
-

# ---
# General
# ---
for each: "for_each = "
depends on: "depends_on = []"
life cycle create before destroy:
    "lifecycle {}"
    key(left enter)
    "create_before_destroy = true"
life cycle prevent destroy:
    "lifecycle {}"
    key(left enter)
    "prevent_destroy = true"
life cycle ignore changes:
    "lifecycle {}"
    key(left enter)
    "ignore_changes = []"
    key(left)

# ---
# AWS data sources/resources
# ---
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
