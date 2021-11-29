from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://EdithKwami:nuku@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class todo(db.Model):
    __tablename__=  "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return (f"<ID: {self.id} description: {self.description}>")

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()["description"]
    todoNew = todo(description = description)
    db.session.add(todoNew)
    db.session.commit()
    return jsonify({
        "description" : todo.description
    })

@app.route('/')
def index():
    return render_template('index.html', data=todo.query.all())


if __name__ == '__main__':
    app.run()
