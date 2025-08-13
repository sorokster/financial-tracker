from flask import Flask
from src.controllers.auth_controller import auth_blueprint
from src.controllers.user_controller import user_blueprint
from src.controllers.category_controller import category_blueprint
from src.controllers.transaction_controller import transaction_blueprint

app = Flask(__name__)
app.secret_key = 'q3E{ku@GO4KE~'

# Register blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(transaction_blueprint)

if __name__ == '__main__':
    INCOME = 1
    SPEND = 2
    app.run(debug=True)