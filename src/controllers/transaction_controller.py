from datetime import datetime
from flask import Blueprint, request, render_template, session, redirect

from src.constants import INCOME, SPEND
from src.decorators.login_required import login_required
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.services.category_service import CategoryService
from src.services.transaction_service import TransactionService

transaction_blueprint = Blueprint('transaction', __name__, url_prefix='')

def get_transaction_service() -> TransactionService:
    return TransactionService(TransactionRepository())

def get_category_service() -> CategoryService:
    return CategoryService(CategoryRepository())

@transaction_blueprint.route('/income', methods=['GET', 'POST'])
@login_required
def incomes():
    owner = session.get('user_id')
    category_service = get_category_service()
    transaction_service = get_transaction_service()

    if request.method == 'GET':
        categories = category_service.get_categories(owner)
        transactions_data = transaction_service.get_incomes(owner)
        return render_template('incomes/index.html', transactions=transactions_data, categories=categories)
    else:
        transaction = transaction_service.create_transaction(
            INCOME,
            float(request.form['amount']),
            int(request.form['category']),
            owner,
            datetime.now(),
            request.form['description'],
        )

        if transaction:
            return redirect('/income')
        return 'Transaction has not been created'


@transaction_blueprint.route('/income/<int:income_id>', methods=['GET', 'POST'])
@login_required
def income(income_id):
    owner = session.get('user_id')
    category_service = get_category_service()
    transaction_service = get_transaction_service()

    if request.method == 'GET':
        categories = category_service.get_categories(owner)
        transaction_data = transaction_service.get_income(income_id, owner)
        if transaction_data is None:
            return render_template('incomes/not_found.html')
        else:
            return render_template('incomes/income.html', transaction=transaction_data, categories=categories)
    else:
        method = request.form.get('_method')
        if method and method.upper() == 'PATCH':
            updated_transaction = transaction_service.update_transaction(
                income_id,
                INCOME,
                float(request.form.get('amount')),
                int(request.form.get('category')),
                owner,
                datetime.now(),
                request.form.get('description'),
            )
            if updated_transaction:
                return redirect('/income/{}'.format(income_id))
            else:
                return 'Transaction has not been updated', 400
        elif method and method.upper() == 'DELETE':
            deleted_transaction = transaction_service.delete_transaction(income_id, owner)
            if deleted_transaction:
                return redirect('/income')
            else:
                return 'Transaction has not been deleted', 400
        else:
            return 'Unsupported method', 400


@transaction_blueprint.route('/spend', methods=['GET', 'POST'])
@login_required
def spends():
    owner = session.get('user_id')
    category_service = get_category_service()
    transaction_service = get_transaction_service()

    if request.method == 'GET':
        categories = category_service.get_categories(owner)
        transactions_data = transaction_service.get_spends(owner)
        return render_template('spends/index.html', transactions=transactions_data, categories=categories)
    else:
        transaction = transaction_service.create_transaction(
            SPEND,
            float(request.form['amount']),
            int(request.form['category']),
            owner,
            datetime.now(),
            request.form['description'],
        )

        if transaction:
            return redirect('/spend')
        return 'Transaction has not been created'

@transaction_blueprint.route('/spend/<int:spend_id>', methods=['GET', 'POST'])
@login_required
def spend(spend_id):
    owner = session.get('user_id')
    category_service = get_category_service()
    transaction_service = get_transaction_service()

    if request.method == 'GET':
        categories = category_service.get_categories(owner)
        transaction_data = transaction_service.get_spend(spend_id, owner)
        if transaction_data is None:
            return render_template('spends/not_found.html')
        else:
            return render_template('spends/spend.html', transaction=transaction_data, categories=categories)
    else:
        method = request.form.get('_method')
        if method and method.upper() == 'PATCH':
            updated_transaction = transaction_service.update_transaction(
                spend_id,
                SPEND,
                float(request.form.get('amount')),
                int(request.form.get('category')),
                owner,
                datetime.now(),
                request.form.get('description'),
            )
            if updated_transaction:
                return redirect('/spend/{}'.format(spend_id))
            else:
                return 'Transaction has not been updated', 400
        elif method and method.upper() == 'DELETE':
            deleted_transaction = transaction_service.delete_transaction(spend_id, owner)
            if deleted_transaction:
                return redirect('/spend')
            else:
                return 'Transaction has not been deleted', 400
        else:
            return 'Unsupported method', 400