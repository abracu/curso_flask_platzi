from multiprocessing import context
from flask import Flask, make_response, redirect, render_template, request

from flask import Flask

app = Flask(__name__)

todos = ['Learn Python', 'Learn Flask', 'Learn React']


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }
    return render_template('hello.html', **context)
