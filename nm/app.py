import admin
import users


import model

from flask import Flask
from flask_bootstrap import Bootstrap4


db = model


app = Flask(__name__)
app.config['TITLE'] = "new Maoo - Titulos"
app.secret_key = b'guerra aos senhores'


admin.configure(app)
users.configure(app)
db.configure(app)

Bootstrap4(app)