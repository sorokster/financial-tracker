from flask import Blueprint, request, render_template, session
from src.decorators.login_required import login_required
from src.factories.database_connection_factory import DatabaseConnectionFactory
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService

user_blueprint = Blueprint('user', __name__, url_prefix='/user')

def get_user_service() -> UserService:
    client = DatabaseConnectionFactory.create_client('sqlite', db_name='financial_tracker.db')
    return UserService(UserRepository(client))

@user_blueprint.route('', methods=['GET', 'DELETE'])
@login_required
def user():
    user_service = get_user_service()
    user_data = user_service.get_user(session['user_email'])
    if request.method == 'GET':
        return render_template('user/user.html', user=user_data)

    if request.method == 'DELETE':
        user_service.delete_user(session['user_id'])
        return 'User deleted'

    return None