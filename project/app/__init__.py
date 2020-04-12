import mysql.connector as mysql
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = mysql.connect(
    host = 'localhost',
    user = 'roland',
    passwd = 'dbms',
    database = 'virus_project'
)
cursor = db.cursor()

from app import routes