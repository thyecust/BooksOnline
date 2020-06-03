# auth 视图
import random
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from BooksOnline.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sex = request.form['sex']
        db = get_db()
        error = None

        if not username:
            error = '请输入用户名'
        elif not password:
            error = '请输入密码'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = '用户名 {} 已经被注册了'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password, sex) VALUES (?, ?, ?)',
                (username, generate_password_hash(password), sex)
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        passcode1 = request.form['passcode1']
        passcode2 = request.form['passcode2']

        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = '用户名错误'
        elif not check_password_hash(user['password'], password):
            error = '密码错误'
        elif passcode1 != passcode2:
            error = '验证码错误'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('explore.index'))

        flash(error)

    passcodes = ['hlia','ikdd','plcc','sdqt']
    passcode = passcodes[random.randint(0,len(passcodes)-1)]
    return render_template('auth/login.html',passcode=passcode)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view