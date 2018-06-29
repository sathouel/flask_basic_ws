from flask import Blueprint, render_template


bp = Blueprint('bv', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about_us.html')


@bp.route('/contact')
def contact():
    return render_template('contact_us.html')
