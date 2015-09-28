# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/25 17:14

import redis

from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from application.models.base import Base, db_session
from application.utils.redis_cli import redis_cli
from application.configure import setting


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, index=True)
    username = Column(String(64), unique=True, index=True)
    password_hash = Column(String(128))
    active = Column(Boolean, default=False)
    avatar_hash = Column(String(32))

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            user = User(email=forgery_py.internet.email_address(),
                        username=forgery_py.internet.user_name(),
                        password=forgery_py.lorem_ipsum.word())

            db_session.add(user)

        try:
            db_session.commit()
        except IntegrityError:
            db_session.rollback()

    def get_id(self):
        return unichr(self.id)

    def is_active(self):
        return self.active

    @property
    def password(self):
        raise AttributeError("User's password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def send_register_mail(self):
        import random
        import string

        from flask import request
        from application.utils.mail.mail_template import get_register_email_content
        from application.utils.mail.send_mail import send_mail

        random.seed()
        key = ".".join(random.sample(string.letters + string.digits, 48))
        redis_cli.set(key, self.id)

        context = {
            "user_name": self.username,
            "host_url": request.host_url or "127.0.0.1:5000",
            "key": key,
            "email": self.email
        }

        email_content = get_register_email_content(**context)
        email_title = u"欢迎加入%s" % setting.APP_NAME
        send_mail = send_mail(email_title, email_content, [self.email])