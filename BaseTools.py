from flask import Flask, render_template, request, redirect, url_for, session, g
from werkzeug import secure_filename


app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'