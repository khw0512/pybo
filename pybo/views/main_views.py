from flask import Blueprint, url_for, g
from werkzeug.utils import redirect
from pybo.views.auth_views import login_required

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
	return 'hello, pybo!@#'

@bp.route('/')
@login_required
def index():
	if g.user is None:
		return redirect(url_for('auth.login'))
	else:
		return redirect(url_for('question._list'))
