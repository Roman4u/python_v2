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
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50))

    def __init__(self, content):
        self.content = content



@app.route('/')
def index():
    all_notes = Notes.query.all()
    print(all_notes)
    return render_template('base.html')


if __name__ == "__main__":
    db.create_all()
    new_note = Notes(content="first test")
    db.session.add(new_note)
    db.session.commit()
    app.run(debug=True)  