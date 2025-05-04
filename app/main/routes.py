from flask import Blueprint, current_app

from flask import render_template, url_for, redirect


bp = Blueprint('main', __name__)


@bp.route("/")
@bp.route("/index")
def index():
    return "<h1>Main page<h1>"
