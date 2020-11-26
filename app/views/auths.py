from flask import Blueprint, render_template, request
from app.forms.registers import RegisterForm

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

    return render_template('auths/register.html', form=form)
