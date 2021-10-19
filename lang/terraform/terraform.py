from talon import ui, Module, Context, registry, actions, imgui, cron
from user.lang.terraform.aws import DATA, RESOURCES

mod = Module()
ctx = Context()

ctx.matches = r"""
title: /.*\.tf/
"""

mod.list("tf_aws_data")
ctx.lists["user.tf_aws_data"] = DATA
mod.list("tf_aws_resources")
ctx.lists["user.tf_aws_resources"] = RESOURCES