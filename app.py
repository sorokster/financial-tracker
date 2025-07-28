from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/user', methods=['GET', 'DELETE'])
def user():
    if request.method == 'GET':
        username = request.args.get('username', 'Guest')
        return render_template('user/user.html', username=username)
    return 'User deleted'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        username = request.form.get('username')
        return f'User {username} is successfully logged in'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        username = request.form.get('username')
        return f'User {username} is successfully registered'

@app.route('/category', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return render_template('categories/index.html')
    return 'Category created'

@app.route('/category/<int:category_id>', methods=['GET', 'PATCH', 'DELETE'])
def category(category_id):
    if request.method == 'GET':
        return render_template('categories/category.html', category_id=category_id)
    elif request.method == 'PATCH':
        return f'Category {category_id} updated'
    return f'Category {category_id} deleted'

@app.route('/income', methods=['GET', 'POST'])
def incomes():
    if request.method == 'GET':
        return render_template('incomes/index.html')
    return 'Income created'

@app.route('/income/<int:income_id>', methods=['GET', 'PATCH', 'DELETE'])
def income(income_id):
    if request.method == 'GET':
        return render_template('incomes/income.html', income_id=income_id)
    elif request.method == 'PATCH':
        return f'Income {income_id} updated'
    return f'Income {income_id} deleted'

@app.route('/spend', methods=['GET', 'POST'])
def spends():
    if request.method == 'GET':
        return render_template('spends/index.html')
    return 'Spend created'

@app.route('/spend/<int:spend_id>', methods=['GET', 'PATCH', 'DELETE'])
def spend(spend_id):
    if request.method == 'GET':
        return render_template('spends/spend.html', spend_id=spend_id)
    elif request.method == 'PATCH':
        return f'Spend {spend_id} updated'
    return f'Spend {spend_id} deleted'

if __name__ == '__main__':
    app.run(debug=True)