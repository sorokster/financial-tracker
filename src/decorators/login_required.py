from functools import wraps
from flask import session, request, url_for, redirect


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            next_url = request.url
            login_url = url_for('auth.login', next=next_url)
            return redirect(login_url)
        return f(*args, **kwargs)
    return decorated_function