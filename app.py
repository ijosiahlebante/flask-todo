from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/api/categories", methods=["GET"])
def get_categories():

    categories = Category.query.all()

    result = []

    for category in categories:
        result.append({
            "id": category.id,
            "name": category.name
        })

    return jsonify(result), 200


@app.route("/api/categories/<int:id>", methods=["GET"])
def get_category(id):

    category = Category.query.get(id)

    if not category:
        return jsonify({
            "error": "Category not found"
        }), 404

    return jsonify({
        "id": category.id,
        "name": category.name
    }), 200


@app.route("/api/categories", methods=["POST"])
def create_category():

    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({
            "error": "Name is required"
        }), 400

    category = Category(name=data["name"])

    db.session.add(category)
    db.session.commit()

    return jsonify({
        "message": "Category created successfully",
        "id": category.id
    }), 201

@app.route("/api/categories/<int:id>", methods=["PUT"])
def update_category(id):

    category = Category.query.get(id)

    if not category:
        return jsonify({
            "error": "Category not found"
        }), 404

    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({
            "error": "Name is required"
        }), 400

    category.name = data["name"]

    db.session.commit()

    return jsonify({
        "message": "Category updated successfully"
    }), 200


@app.route("/api/categories/<int:id>", methods=["DELETE"])
def delete_category(id):

    category = Category.query.get(id)

    if not category:
        return jsonify({
            "error": "Category not found"
        }), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({
        "message": "Category deleted successfully"
    }), 200

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
