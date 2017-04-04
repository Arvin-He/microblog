from flask import render_template
from app import app


# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'Arvin'}
#     return render_template("index.html", title='Home', user=user)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Arvin'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movies was so cool!'
        }]
    return render_template("index.html", title='Home', user=user,posts=posts)