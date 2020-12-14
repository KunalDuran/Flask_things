from flask import Blueprint, render_template


batsman = Blueprint('batsman', __name__, template_folder='templates')


@batsman.route("/batsman")
def bat():
    return render_template('batsman.html')