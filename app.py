from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
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
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    all_notes = Notes.query.all()
    print(all_notes)
    return render_template('base.html', all_notes=all_notes)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_note = Notes(content=title, complete=False)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:note_id>", methods=["POST"])
def update_note(note_id):
    note = Notes.query.filter_by(id=note_id).first()
    note.complete = not note.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/remove/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    print("I'm here") 
    note = Notes.query.filter_by(id=note_id).first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("index"))



if __name__ == "__main__":
    db.create_all()


    app.run(debug=True)  