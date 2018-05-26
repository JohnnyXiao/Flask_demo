from flask import render_template
from app import app

@app.route('/')
@app.route('/index_for')
def index():
	user = { 'nickname': 'Xiaoyong' }
	posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': { 'nickname': 'xiaoyong'},
            'body': 'this is a blog content'
        },
        {
            'author': { 'nickname': 'xiaoyong2'},
            'body': 'this is a blog content........'
        }
    ]
	return render_template("index_for.html", title = 'Home', user = user, posts = posts)