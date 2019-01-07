# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.24
    @version: 1.0
    @desc: 表单类，定义各种需要用到的表单
'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
    BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Optional, URL

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('记住密码')
    submit = SubmitField('登陆')
