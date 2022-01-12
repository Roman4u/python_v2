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

   


db.create_all() 

@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    item = Notes.query.get(id)
    del item.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)

@app.route('/items', methods=['GET'])
def get_items():
    items = []
    # for item in db.session.query(Notes).all():
    #     del item.__dict__['_sa_instance_state']
    #     items.append(item.__dict__)
    return jsonify(items)
    # return jsonify("the get method is possibly working")

# @app.route('/items', methods=['POST'])
# def create_item():
#     body = request.get_json()
#     db.session.add(Notes(body['content']))
#     db.session.commit()
#     return "item created"

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    body = request.get_json()
    db.session.query(Notes).filter_by(id=id).update(
        dict(content = body['content'])
    )
    db.session.commit()
    return "item updated"

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    db.session.query(Notes).filter_by(id=id).delete()
    db.session.commit()
    return " item deleted"

@app.route('/')
def index():
    return render_template('base.html')


if __name__ == "__main__":
      app.run(debug=True)  