import os
from flask import Flask, jsonify, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_OLIVE_URL']
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Integer)

    def __init__(self, answer):
        self.answer = answer

    def __repr__(self):
        return '<User {0}>'.format(self.answer)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_answer_linda', methods=['POST'])
def linda():
    answer = request.form.get('answer', 99)
    participant = User(answer)
    db.session.add(participant)
    db.session.commit()
    return jsonify({"success" : answer})
