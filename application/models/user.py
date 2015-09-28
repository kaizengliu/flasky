# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/25 17:14

from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from base import Base, db_session


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
    def password(self, _password):
        self.password_hash = generate_password_hash(_password)

