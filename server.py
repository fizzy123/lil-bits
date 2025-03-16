import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_socketio import SocketIO

import settings

app = Flask(__name__)
app.config.from_object(settings)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)
csrf = CSRFProtect(app)

#pylint: disable=wrong-import-position
import views
