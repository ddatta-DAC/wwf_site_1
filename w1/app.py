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

@app.route('/trade_by_year')
def trade_by_year():
    return render_template('trade_by_year.html')

@app.route('/graph_analysis_1')
def graph_analysis_1():
    return render_template('graph_analysis_1.html')


@app.route('/graph_analysis_2')
def graph_analysis_2():
    return render_template('graph_analysis_2.html')