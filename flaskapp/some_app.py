from flask import Flask
app = Flask(__name__)




# Декоратор для вывода страницы по умолчанию
@app.route('/')
def hello():
    return '<html><head></head><body><h1>Hello World!</h1></body></html>'

# функция сайта по ссылке http://127.0.0.1:5000/data_to
@app.route('/data_to')
def data_to():
    some_pars = {'user':'Dmitriy','color':'red'}
    some_str = 'Hello my dear friends!'
    some_value = 10

    # Данные передадим в шаблон и вызовем его
    return render_template('simple.html',some_str=some_str,some_value=some_value,some_pars=some_pars)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)