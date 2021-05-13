from flask import Flask
from datetime import time, timedelta
from route.fc import fc, db

app = Flask(__name__)
app.register_blueprint(fc)
app.secret_key = 'thisisverysecretnot'
app.permanent_session_lifetime = timedelta(minutes=5)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flash_card.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login')
# def login():
#     return "<h1>This is going to be the login page </h1>"


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)