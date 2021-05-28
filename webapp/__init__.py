from .route.fc import flash_card, add_flashcard, fc_index, view, pop_fc, delete, update, edit, practice, cancel, fc, db

from flask import Flask
from datetime import time, timedelta

app = Flask(__name__)
app.register_blueprint(fc)
app.secret_key = 'thisisverysecretnot'
app.permanent_session_lifetime = timedelta(minutes=5)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flash_card.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

