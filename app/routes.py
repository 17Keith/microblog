from flask import render_template
from app import app

# Use render_template() function

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Keith'}
    posts= [
        {
            'author': {'username': 'John'},
            'body': 'Today is going to be a beautiful day!'
        },
        {
            'author': {'username': 'Doe'},
            'body': 'My dog just gave birth.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
