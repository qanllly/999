import json
import os
import csv

class Book:
    __count = 0 

    def __init__(self, title, author, year, isbn, genre, pages):
        if not isinstance(year, int) or year > 2026:
            raise ValueError("год издания должен быть целым числом не из будущего")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("количество страниц должно быть положительным числом")
        
        Book.__count += 1
        self.__id = Book.__count
        
        self.title = str(title)
        self.author = str(author)
        self.year = year
        self.isbn = str(isbn)
        self.genre = str(genre)
        self.pages = pages
        print(f"создание Книги ID {self.__id}")

    def __del__(self):
        print(f"удаление Книги ID {self.__id}")

    def __str__(self):
        return f"[{self.__id}] '{self.title}' - {self.author} ({self.year}) | Жанр: {self.genre} | Стр: {self.pages}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.isbn}')"

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    def __copy__(self):
        return Book(self.title, self.author, self.year, self.isbn, self.genre, self.pages)

    def to_dict(self):
        return {
            "title": self.title, "author": self.author, "year": self.year,
            "isbn": self.isbn, "genre": self.genre, "pages": self.pages
        }

DB_PATH = "library.json"

def save_db(books):
    data = [b.to_dict() for b in books]
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Book(i['title'], i['author'], i['year'], i['isbn'], i['genre'], i['pages']) for i in data]

def export_to_csv(books, filename="library_export.csv"):
    if not books:
        return
    with open(filename, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Название", "Автор", "Год", "ISBN", "Жанр", "Страницы"])
        for b in books:
            writer.writerow([b.title, b.author, b.year, b.isbn, b.genre, b.pages])

def sort_pyz(books, field):
    n = len(books)
    for i in range(n):
        for j in range(0, n - i - 1):
            if field == "year":
                if books[j+1] < books[j]:
                    books[j], books[j+1] = books[j+1], books[j]
            else:
                val1 = getattr(books[j], field)
                val2 = getattr(books[j+1], field)
                if str(val1).lower() > str(val2).lower():
                    books[j], books[j+1] = books[j+1], books[j]