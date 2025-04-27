from urllib import request
from flask import render_template,blueprints,redirect,url_for,flash,request,session
from flask_login import login_required
from sqlalchemy import false

from  leande import login_manager
from leande.controller import my_database
from flask_login import login_required,logout_user,current_user

main = blueprints.Blueprint('main', __name__)
login_manager.login_view = 'main.login'

@main.route('/')
def index():
    log=False
    if session.get('logged_in'):
        log=True
    return render_template('index.html',log=log)

@main.route('/videocall')
@login_required
def videocall():
    return  render_template('videocall.html')

@main.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        pw = request.form['pw']

        if my_database.login(name,pw):
            session['logged_in'] = True
            return redirect(url_for('main.index'))
        else:
            flash('mat khau khong khop')
    return render_template('login.html')

@main.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        pw = request.form['pw']
        cpw = request.form['cpw']

        if pw != '' and cpw != '' and pw==cpw:
            my_database.add_account(name,pw)
        else:
            flash('mat khau khong chinh xac')
    return redirect(url_for('main.login'))

@main.route('/logout')
def logout():
    logout_user()
    session.pop('logged_in', None)
    return redirect(url_for('main.index'))
