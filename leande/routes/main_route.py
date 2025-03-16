from flask import render_template,blueprints

main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')