# -*- coding: utf-8 -*-
from BaseTools import redirect, session, url_for
from BaseTools import secure_filename
import os


def register_success(user_name):
    return redirect(url_for('index'))


def register_fail(user_name):
    pass


def login_success(user_name):
    session['logged_in'] = True
    return redirect(url_for('index', username=user_name))


def login_fail(user_name):
    pass


def upload_file_success(file, file_saved_path):
    filename = secure_filename(file.filename)
    file.save(os.path.join(file_saved_path, filename))
    return

