from flask import Flask, make_response, redirect, request

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@ app.route('/hello')
def hello_world():
    user_ip = request.cookies.get('user_ip')
    return 'Hello World! tu IP es: {}'.format(user_ip)
