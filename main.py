from flask import Flask, render_template, request, redirect, url_for
from book import Book



app = Flask(__name__)

books = [Book("Book1", "Author1", "Fiction"), 
         Book("Book2", "Author2", "Non-Fiction"),
         Book("Book3", "Author3", "Science"),
         Book("Book4", "Author4", "History")]

@app.route('/')
def home():
    if request.args.get('search_name'):
        name = request.args.get('search_name')
        return render_template('index.html', books=[book for book in books if book.name == name])
    return render_template('index.html', books=books)

@app.route('/add_book')
def add_book():
    pass


if __name__ == "__main__":
    app.run(debug=True)