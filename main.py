from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

todos = [{'task': 'Sample', 'done': False}]

@app.route("/")
def TodoApp():
    x = datetime.now()
    dateandtime = x.strftime("%A, %d %B,  %Y")
    return render_template("index.html", todos=todos, datetime=dateandtime)


@app.route("/add", methods=['GET', 'POST'])
def add():
    todo = request.form.get("task")
    todos.append({'task':todo, 'done':False})
    return redirect(url_for("TodoApp"))

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('TodoApp'))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("TodoApp"))


if __name__ == "__main__":
    app.run(debug=True)