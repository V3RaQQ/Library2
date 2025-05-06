from flask import Flask, render_template, request, redirect, url_for
from book import Book



app = Flask(__name__)

books = []

@app.route('/')
def home():
    return render_template('index.html', books=books)





if __name__ == "__main__":
    app.run(debug=True)