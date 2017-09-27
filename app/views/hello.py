from flask import render_template

from . import views


@views.route("/")
def hello():
	return render_template('index.html')
