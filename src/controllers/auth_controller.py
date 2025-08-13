from flask import Blueprint, request, render_template, session, redirect, url_for
from src.decorators.anonymous_required import anonymous_required
from src.factories.database_connection_factory import DatabaseConnectionFactory
from src.repositories.user_repository import UserRepository
from src.services.auth_service import AuthService

auth_blueprint = Blueprint('auth', __name__, url_prefix='')

def get_auth_service() -> AuthService:
    client = DatabaseConnectionFactory.create_client('sqlite', db_name='financial_tracker.db')
    return AuthService(UserRepository(client))

@auth_blueprint.route('/register', methods=['GET', 'POST'])
@anonymous_required
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        email = request.form.get('email')
        name = request.form.get('name')
        surname = request.form.get('surname')
        password = request.form.get('password')

        auth_service = get_auth_service()
        success = auth_service.register(email, name, surname, password)

        if success:
            return f'User with email: {email} is successfully registered'
        else:
            return 'Registration failed', 400

@auth_blueprint.route('/login', methods=['GET', 'POST'])
@anonymous_required
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        auth_service = get_auth_service()
        user = auth_service.authenticate(email, password)

        if user:
            session['user_id'] = user.id
            session['user_email'] = user.email

            return redirect('/user')
        else:
            return 'Invalid credentials', 401

@auth_blueprint.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    return redirect(url_for('auth.login'))