from flask import render_template, request, session, redirect, url_for
from app import app
from flask_mail import Mail, Message

mail = Mail(app)
# instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nkjcgpt@gmail.com'
app.config['MAIL_PASSWORD'] = 'hpwsarpxwwxfcrbe'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
@app.route('/index')
def index():
    return "Hello World"