# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 16:31

import os

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader


def _get_template_path():
    mail_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(mail_dir, "templates")

loader = FileSystemLoader(_get_template_path())
env = Environment(loader=loader)


def get_register_email_content(**kwargs):
    return env.get_template('register.html').render(kwargs)