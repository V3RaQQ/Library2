from flask import Flask, render_template, request, redirect, url_for
from book import Book



app = Flask(__name__)


books = [Book('name', 'fheiwo', 'fhjewuiof')]


@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route("/remove/<name>")
def remove(name):
    if name in [book.name for book in books]:
        for book in books:
            if book.name == name:
                books.remove(book)
                print(f'removed book {book.name}')
                return redirect(url_for('home'))
    print('not finded')
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)