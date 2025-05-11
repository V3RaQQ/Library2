from flask import Flask, render_template, request, redirect, url_for
from book import Book


d = {"a": 5, "b": 10}


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
    if request.args.get('search_name'):
        name = request.args.get('search_name')
        return render_template('index.html', books=[book for book in books if book.name == name])
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

@app.route('/edit_book')
def edit_book():
    name = request.args.get('book_name')
    print(name)
    editing_book = None
    for book in books:
        if book.name == name:
            editing_book = book
    return render_template('edit_book.html', book=editing_book)

@app.route('/edit', methods=['POST'])
def edit():
    old_name = request.form['old_name']
    name = request.form['name']
    author = request.form['author']
    category = request.form['category']
    for book in books:
        if book.name == old_name:
            book.name = name
            book.author = author
            book.category = category
            return render_template('index.html', books=books)
    print('error')
    return render_template('index.html', books=books)

if __name__ == "__main__":
    app.run(debug=True)