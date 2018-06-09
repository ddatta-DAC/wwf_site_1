from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/login')
def login():
    return 'login'

@app.route('/companies')
def companies():
    return render_template('companies.html')

