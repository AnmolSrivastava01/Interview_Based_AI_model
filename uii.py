from flask import Flask, render_template

from docx import Document

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

def save_to_word(text):
    document = Document()
    document.add_paragraph(text)
    document.save("output.docx")

@app.route("/save_text/<text>")

def save_text(text):
    save_to_word(text)
    return "Text saved to Word file."

if __name__ == "__main__":
    app.run(debug=True)
