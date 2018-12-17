from flask import Blueprint, request, render_template

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    print("Home")
    return render_template('test.html', template_folder='../templates')