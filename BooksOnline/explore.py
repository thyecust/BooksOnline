# explore 视图
import os
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from BooksOnline.auth import login_required
from BooksOnline.db import get_db

bp = Blueprint('explore', __name__)

@bp.route('/', methods=('GET','POST'))
def index():
    n = request.args.get('n')
    if not n:
        n = 0
    else:
        n = int(n)
        if n-5<0:
            n = 0
    db = get_db()
    books = db.execute(
        'SELECT p.id, title, description, created, owner, price, discount, amount, username, picture'
        ' FROM book p JOIN user u ON p.owner = u.id'
        ' ORDER BY created DESC LIMIT 5 OFFSET ?',
        (n,)
    ).fetchall()
    return render_template('explore/index.html', books=books, n=n)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        picture = request.files['picture']
        description = request.form['description']
        price = request.form['price']
        discount = request.form['discount']
        amount = request.form['amount']

        error = None

        if not title:
            error = 'Title is required.'
        elif picture.filename == '':
            error = '请上传图片。'

        if error is not None:
            flash(error)
        else:
            filename = secure_filename(picture.filename)
            picture.save(os.path.join('BooksOnline\static\img\\book', filename))
            db = get_db()
            db.execute(
                'INSERT INTO book (picture,owner,price,discount,amount,description,title)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?)',
                (filename,g.user['id'],price,discount,amount,description,title)
            )
            db.commit()
            return redirect(url_for('explore.index'))

    return render_template('explore/create.html')

def get_book(id, check_author=True):
    book = get_db().execute(
        'SELECT b.id, title, description, created, owner, price, discount, amount, username, picture'
        ' FROM book b JOIN user u ON b.owner = u.id'
        ' WHERE b.id = ?',
        (id,)
    ).fetchone()

    if book is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    # if check_author and book['owner'] != g.user['id']:
    #     abort(403)

    return book

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    book = get_book(id)

    if request.method == 'POST':
        title = request.form['title']
        picture = request.files['picture']
        print(bool(picture.filename))
        description = request.form['description']
        price = request.form['price']
        discount = request.form['discount']
        amount = request.form['amount']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        elif not picture.filename:
            print('hi')
            db = get_db()
            db.execute(
                'UPDATE book SET title = ?, description = ?, price = ?, discount = ?, amount = ?'
                ' WHERE id = ?',
                (title, description, price, discount, amount, id)
            )
            db.commit()
            return redirect(url_for('explore.index'))
        else:
            filename = picture.filename
            picture.save(os.path.join('BooksOnline\static\img\\book', filename))
            db = get_db()
            db.execute(
                'UPDATE book SET title = ?, picture = ?, description = ?, price = ?, discount = ?, amount = ?'
                ' WHERE id = ?',
                (title, filename, description, price, discount, amount, id)
            )
            db.commit()
            return redirect(url_for('explore.index'))

    return render_template('explore/update.html', book=book)

@bp.route('/<int:id>/description',methods=('GET','POST'))
@login_required
def description(id):
    book = get_book(id)
    return render_template('explore/description.html', book=book)

@bp.route('/<int:id>/delete', methods=('POST','GET'))
@login_required
def delete(id):
    print('hello1')
    get_book(id)
    db = get_db()
    db.execute('DELETE FROM book WHERE id = ?', (id,))
    db.commit()
    print('hello2')
    return redirect(url_for('explore.index'))