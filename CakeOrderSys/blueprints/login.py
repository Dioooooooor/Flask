# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.15
    @version: 1.0
    @desc: 登陆视图
'''

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from CakeOrderSys.forms import LoginForm
from CakeOrderSys.utils import redirect_back
from CakeOrderSys.models import Admin

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('manager.managerhome'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect(url_for('manager.managerhome'))
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('login/login.html', form=form)

@login_bp.route('/logout')
def logout():
    return 'hello world!'