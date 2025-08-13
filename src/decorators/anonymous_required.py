from functools import wraps
from flask import session, redirect


def anonymous_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' in session:
            return redirect('/user')
        return f(*args, **kwargs)
    return decorated_function