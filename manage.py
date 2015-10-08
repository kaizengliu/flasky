# -*-coding: utf-8-*-
# time: 2015/09/16 22:38
# author: liukaizeng

from flask.ext.script import Manager
from application import app

manager = Manager(app)

import migrate

if __name__ == '__main__':
    manager.run()
