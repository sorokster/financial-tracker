from flask import Blueprint, request, render_template, session, redirect
from src.decorators.login_required import login_required
from src.repositories.category_repository import CategoryRepository
from src.services.category_service import CategoryService

category_blueprint = Blueprint('category', __name__, url_prefix='/category')

def get_category_service() -> CategoryService:
    return CategoryService(CategoryRepository())

@category_blueprint.route('', methods=['GET', 'POST'])
@login_required
def categories():
    owner = session.get('user_id')
    category_service = get_category_service()

    if request.method == 'GET':
        categories_data = category_service.get_categories(owner)
        return render_template('categories/index.html', categories=categories_data)
    else:
        new_category = category_service.create_category(request.form.get('name'), owner)
        if new_category:
            return redirect('/category/{}'.format(new_category.id))
        return 'Category has not been created'

@category_blueprint.route('/<int:category_id>', methods=['GET', 'POST'])
@login_required
def category(category_id):
    owner = session['user_id']
    category_service = get_category_service()

    if request.method == 'GET':
        category_data = category_service.get_category(category_id, owner)
        if category_data is None:
            return render_template('categories/not_found.html')
        else:
            return render_template('categories/category.html', category=category_data)
    else:
        method = request.form.get('_method')
        if method and method.upper() == 'PATCH':
            updated_category = category_service.update_category(category_id, request.form.get('name'), owner)
            if updated_category:
                return redirect('/category/{}'.format(category_id))
            else:
                return 'Category has not been updated', 400
        elif method and method.upper() == 'DELETE':
            deleted_category = category_service.delete_category(category_id, owner)
            if deleted_category:
                return redirect('/category')
            else:
                return 'Category has not been updated', 400
        else:
            return 'Unsupported method', 400