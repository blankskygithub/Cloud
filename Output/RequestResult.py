# -*- coding: utf-8 -*-
from BaseTools import redirect, session, url_for


def register_success(user_name):
    pass


def register_fail(user_name):
    pass


def login_success(user_name):
    session['logged_in'] = True
    return redirect(url_for('index', username=user_name))


def login_fail(user_name):
    pass
