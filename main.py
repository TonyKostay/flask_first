from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config ['SECRET_KEY'] = 'fffjjdhhndj33s8fc8d3d'
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

app.run(debug=True)

