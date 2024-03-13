from flask import Blueprint, render_template
from flask import flash, redirect, url_for

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

# @site.route('/some_route')
# def some_route():
#     flash('Welcome to the KOC lab!', 'success')
#     return redirect(url_for('site.home'))

# @site.route('/flash_page')
# def flash_page():
#     return render_template('flash.html')

# @site.route('/flash/<message>')
# def flash(message):
#     return render_template("flash.html", msg = message)