from flask import render_template, request, session, redirect, url_for
from app import app
import modeFunctions as mf
import time


@app.route('/')
def index():
    return render_template('index.html', toggleValue=mf.get_current_mode())


@app.route('/mode_switch', methods=["GET", "POST"])
def mode_switch():

    data = request.form.get("mode")
    mf.push_new_mode(data)
    print(mf.get_current_mode())

    return data
