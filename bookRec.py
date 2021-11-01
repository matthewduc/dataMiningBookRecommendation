import numpy as np
import pandas as pd
books = pd.read_csv("Books.csv", sep=';', encoding="latin-1", error_bad_lines=False)
users = pd.read_csv("Users.csv", sep=';', encoding="latin-1", error_bad_lines=False)
ratings = pd.read_csv("Ratings.csv", sep=';', encoding="latin-1", error_bad_lines=False)
books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]
books.rename(columns = {'Book-Title':'title', 'Book-Author':'author', 'Year-Of-Publication':'year', 'Publisher':'publisher'}, inplace=True)
users.rename(columns = {'User-ID':'user_id', 'Location':'location', 'Age':'age'}, inplace=True)
ratings.rename(columns = {'User-ID':'user_id', 'Book-Rating':'rating'}, inplace=True)
