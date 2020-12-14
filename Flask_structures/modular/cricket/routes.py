from cricket import app
from flask import render_template


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/batsman")
def batsman():
    return  render_template('batsman.html')


@app.route("/bowler")
def bowler():
    return  render_template('bowler.html')