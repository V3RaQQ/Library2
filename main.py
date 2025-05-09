from flask import Flask, render_template, request, redirect, url_for
from book import Book



app = Flask(__name__)

books = [Book("Book1", "Author1", "Fiction"), 
         Book("Book2", "Author2", "Non-Fiction"),
         Book("Book3", "Author3", "Science"),
         Book("Book4", "Author4", "History")]
categories = []
for book in books:
    categories.append(book.category)
print(categories)


@app.route('/')
def home():
    return render_template('index.html', books=books, categories=categories)

@app.route('/add_book', methods=['POST'])
def add_book():
    pass




if __name__ == "__main__":
    app.run(debug=True)