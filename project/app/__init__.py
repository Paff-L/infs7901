from flask import Flask
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap
from config import Config
import mysql.connector as mysql

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect()
csrf.init_app(app)
db = mysql.connect(
    host = 'localhost',
    user = 'roland',
    passwd = 'dbms',
    database = 'virus_project'
)
cursor = db.cursor()
bootstrap = Bootstrap(app)

from app import routes, models, errors