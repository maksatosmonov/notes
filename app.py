from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    notes_file = open("notes.txt", "r", encoding="utf-8")
    notes_list = [row for row in notes_file]
    notes_file.close
    return render_template("index.html", notes_list=notes_list)

@app.route("/hello/<string:user_name>")
def hello(user_name):
    user_name = user_name.capitalize()
    return render_template("hello.html", user_name=user_name)

@app.route("/add-note-form")
def add_note_form():
    return render_template("add_note_form.html")

@app.route("/add-note", methods=["POST"])
def add_note():
    note = request.form["new-note"]
    notes_file = open("notes.txt", "a+", encoding="utf-8")
    notes_file.write(note + "\n")
    notes_file.close()
    return render_template("success.html")






