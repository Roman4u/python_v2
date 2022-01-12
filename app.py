from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import psycopg2



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://romanmontoya@127.0.0.1:5432/flask_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Notes(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, content):
        self.content = content



@app.route('/')
def index():
    #show all notes
    # notes = Notes.query.all()
    return render_template('base.html')

@app.route('/test')
def message():
    return "Hello"

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)  