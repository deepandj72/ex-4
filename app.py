from flask import Flask, render_template, request, redirect

app = Flask(__name__)
notes = []   # store notes in memory

@app.route("/")
def home():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    note_text = request.form["note"]
    if note_text.strip():
        notes.append(note_text)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
