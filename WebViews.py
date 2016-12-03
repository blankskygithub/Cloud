import BaseTools
from BaseTools import app
from BaseTools import render_template
from BaseTools import url_for


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
@app.route('/index/<username>')
def index(username=None):
    return render_template('index.html', username=username)


@app.route('/user/<username>')
def user_profile(username=None):
    return render_template('personalPage.html', username=username)



