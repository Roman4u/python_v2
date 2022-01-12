from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://romanmontoya@localhost:5000/DATABASE_URL'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, content):
        self.content = content


# db.create_all() 

# @app.route('/items/<id>', methods=['GET'])
# def get_item(id):
#     item = Item.query.get(id)
#     del item.__dict__['_sa_instance_state']
#     return jsonify(item.__dict__)

@app.route('/items', methods=['GET'])
def get_items():
    # items = []
    # for item in db.session.query(Item).all():
    #     del item.__dict__['_sa_instance_state']
    #     items.append(item.__dict__)
    # return jsonify(items)
    return jsonify("the get method is possibly working")

# @app.route('/items', methods=['POST'])
# def create_item():
#     body = request.get_json()
#     db.session.add(Item(body['content']))
#     db.session.commit()
#     return "item created"

# @app.route('/items/<id>', methods=['PUT'])
# def update_item(id):
#     body = request.get_json()
#     db.session.query(Item).filter_by(id=id).update(
#         dict(content = body['content'])
#     )
#     db.session.commit()
#     return "item updated"

# @app.route('/items/<id>', methods=['DELETE'])
# def delete_item(id):
#     db.session.query(Item).filter_by(id=id).delete()
#     db.session.commit()
#     return " item deleted"

@app.route('/')
def index():
    return "Hello"
    # render_template('base.html')


if __name__ == "__main__":
      app.run(debug=True)  