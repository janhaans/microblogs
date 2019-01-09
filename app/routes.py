from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jan Haans'}
    posts = [   {'author': 'Anna-Maria','body': 'Some text from Anna-Maria'},
                {'author': 'Valentina', 'body': 'Some text from Valentina'}
            ]
    return render_template("index.html", user=user, posts=posts)