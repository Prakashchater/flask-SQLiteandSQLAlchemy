# import sqlite3
#
# db = sqlite3.connect('books-collection.db')
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books ("
# #                "id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE,"
# #                "author varchar(250) NOT NULL, "
# #                "rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(2, 'Harri Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
#
# ##CREATE DATABASE
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# # Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# ##CREATE TABLE
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#
#     # Optional: this will allow each book object to be identified by its title when printed.
#     def __repr__(self):
#         return f'<User> {self.title}'
#
# db.create_all()
#
#
# ##CREATE RECORD
# new_book = User(id=2, title="Harry Putter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE
class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()

##CREATING NEW RECORD
new_book = books(id=1, title='Avengers Endgame', author='Prakash', rating='10')
db.session.add(new_book)
db.session.commit()


##READ ALL THE RECORDS
all_books = db.session.query(books).all()

##Read A Particular Record By Query
book = books.query.filter_by(title="Avengers Endgame").first()

# Update A Particular Record By Query
book_to_update = books.query.filter_by(title="Avengers Endgame").first()
book_to_update.title = "Avengers Infinity War"
db.session.commit()

# Update A Record By PRIMARY KEY
book_id = 1
book_to_update = books.query.get(book_id)
book_to_update.title = "Avengers Age of Ultron"
db.session.commit()

# Delete A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = books.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()














