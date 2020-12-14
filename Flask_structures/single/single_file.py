from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    
    return '<h1>Hello Kunal Duran</h1>'


@app.route("/batsman")
def batsman():
    return '<h1>I am a Batsman</h1>'


@app.route("/bowler")
def bowler():
    return '''<h1>Leg Spinner</h1>
    <ul>
        <li>Economy: 5.33</li>
        <li>Best: 5 for 31 in 10 overs</li>
    </ul>
    '''


if __name__ == "__main__":
    app.run(debug=True)