from flask import Flask, render_template, url_for, request, flash, session, redirect, abort
import sqlite3
import os

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fffjjdhhndj33gitgits8fc8d3d'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
products = {'7': 'iphone-7', '8': 'iphone-8',
            '10': 'iphone-10', '10+': 'iphone-10+',
            '11': 'iphone-11', '11 pro max': 'iphone-11-pro-max',
            '12': 'iphone-12', '12 mini': 'iphone-12-mini'}
products2 = {'MacBook PRO': 'MacBook-PRO', 'MacBook Air': 'MacBook-Air',
             'iMac': 'iMac'}
def processing(method,form):
    if method == 'POST':
        print(form)
        if len(form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')


@app.route('/', methods=['POST','GET'])
def index():
    processing(request.method, request.form)
    return render_template('index.html', title="Смартфоны Apple Iphone", products=products, link='/page2', text_link='Перейти к компьютерам', action='/')

@app.route('/page2', methods=['POST','GET'])
def page2():
    processing(request.method, request.form)
    return render_template('page2.html', title="Ноутбуки и компьютеры Apple", products=products2, link='/', text_link='Перейти к смартфонам',action='/page2')

@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        return render_template('login.html', title='Авторизация')
    return f'Профиль пользователя: {username}'

@app.route('/login', methods=["POST","GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "selfedu" and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация')


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена'), 404


app.run(debug=True)

