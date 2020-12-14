from flask import Blueprint, render_template


bowler = Blueprint('bowler', __name__)


@bowler.route("/bowler")
def bowl():
    return render_template('bowler.html')