# check 视图
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from BooksOnline.db import get_db
from BooksOnline.auth import login_required
from BooksOnline.explore import get_book

bp = Blueprint('check', __name__, url_prefix='/check')

def get_cart_book(user,book):
    db = get_db()
    cart_book = db.execute(
        'SELECT id FROM cart WHERE user=? AND book=?',
        (user,book)
    ).fetchall()
    return cart_book

@bp.route('/add', methods=('POST','GET'))
@login_required
def add():
    book = request.args.get('id')
    user = g.user['id']
    cart_book = get_cart_book(user,book)
    print(cart_book)
    if cart_book is not None:
        print(cart_book)
        flash('已经添加过了')
    db = get_db()
    db.execute(
        'INSERT INTO cart (user,book) VALUES (?,?)',
        (user,book)
    )
    db.commit()
    flash("成功加入购物车")
    return redirect(url_for('explore.index'))

@bp.route('/', methods=('GET','POST'))
@login_required
def cart():
    user = g.user['id']
    db = get_db()
    books = db.execute(
        'SELECT b.id,picture,title,price,description,amount,discount'
        ' FROM cart c JOIN book b ON c.book = b.id'
        ' WHERE c.user=? ORDER BY c.created DESC ',
        (user,)
    ).fetchall()
    return render_template('check/cart.html', books=books)
