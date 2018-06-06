from flask import Flask, render_template, url_for, request, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/table/')
def table():
    with open('./static/table.txt', 'r') as f:
        l = list(f)
        info = {}
        info['username'] = l[0]
        info['age'] = l[1]
        info['sex'] = l[2]
    return info


@app.route('/table1/', methods=['POST', 'GET'])
def table1():
    render_template('table.html')


@app.route('/search/')
def search():
    return render_template('search.html')


# 默认的视图函数值能采用get请求
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        return 'hhh'


if __name__ == '__main__':
    app.run(debug=True)
