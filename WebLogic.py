import BaseTools
from BaseTools import app
from BaseTools import request
from BaseTools import render_template
from Input import Check
from Output import RequestResult


@app.route('/resister', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if Check.is_user_name_valid_register():
            return RequestResult.register_success(request.form['username'])
        else:
            return RequestResult.register_fail(request.form['username'])
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if Check.is_access_token_valid_login(request.form['username'], request.form['password']):
            return RequestResult.login_success(request.form['username'])
        else:
            return RequestResult.login_fail(request.form['username'])
    return render_template('login.html')

