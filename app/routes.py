from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# Use render_template() function


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Keith'}
    posts = [
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

# New Login Route for the app!


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
