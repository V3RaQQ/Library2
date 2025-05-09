from flask import Flask, render_template, request, redirect, url_for
from book import Book



app = Flask(__name__)

books = [Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
        Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
        Book("1984", "George Orwell", "Dystopian")]

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    name = request.form['name']
    author = request.form['author']
    category = request.form['category']
    if category == 'null':
        return render_template('index.html', books=books)
    new_book = Book(name, author, category)
    books.append(new_book)
    return redirect(url_for('home'))

#remove branch




if __name__ == "__main__":
    app.run(debug=True)