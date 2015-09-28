# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 17:51

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo

from application.models.user import User


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(u'邮箱不能为空')], description=u"注册时所用邮箱")
    password = StringField(u'密码', validators=[DataRequired(u'密码不能为空'), Email], description=u"密码")

    def validate_email(form, field):
        email = field.data.strip().lower()

        email_existed = User.query.filter(User.email == email).count() > 0

        if not email_existed:
            raise ValidationError(u'邮箱不存在')

    def validate_password(form, field):
        email = form.email.data.strip().lower()
        password = field.data.strip()

        user = User.query.filter(User.email == email).one()
        if not user.verify_password(password):
            raise ValidationError(u'密码错误')