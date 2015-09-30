# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 17:51

from flask.ext.wtf import Form
from flask.ext.login import login_user
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo

from application.models.user import User


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(u'邮箱不能为空'), Email()], description=u"注册时所用邮箱")
    password = PasswordField(u'密码', validators=[DataRequired(u'密码不能为空')], description=u"密码")

    def validate_email(form, field):
        email = field.data.strip().lower()

        email_existed = User.query.filter(User.email == email).count() > 0

        if not email_existed:
            raise ValidationError(u'邮箱不存在')

    def validate_password(form, field):
        email = form.email.data.strip().lower()
        password = field.data.strip()

        user = User.query.filter(User.email == email).first()

        if not user:
            return

        if not user.verify_password(password):
            raise ValidationError(u'密码错误')

        login_user(user)


class RegisterForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(u'邮箱不能为空'), Email()], description=u'邮箱')
    password = PasswordField(u'密码',
                           validators=[
                               DataRequired(u'密码不能为空'),
                               Length(min=6, max=20, message=u'密码长度在6位到20位之间')
                           ],
                           description=u'密码')
    password_check = PasswordField(u'密码确认',
                                 validators=[
                                     DataRequired(u'请再次确认密码'),
                                     EqualTo('password', message=u'两次输入的密码不一致')
                                 ],
                                 description=u'密码确认')

    def validate_email(form, field):
        email = field.data.strip().lower()

        email_has_be_registered = User.query.filter(User.email == email).count() > 0

        if email_has_be_registered:
            raise ValidationError(u'该邮箱已经被注册')
