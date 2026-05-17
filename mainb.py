import csv
from book import Book, load_db, save_db, sort_pyz

def print_menu():
    print("\nМЕНЮ БАЗЫ ДАННЫХ КНИГ")
    print("1 просмотр всех записей")
    print("2 добавление книги")
    print("3 поиск книги")
    print("4 редактирование (изменение количества страниц)")
    print("5 удаление книги")
    print("6 сортировка")
    print("7 экспорт в CSV")
    print("0 выход")

def main():
    db = load_db()
    
    if not db:
        db = [
            Book("1984", "Джордж Оруэлл", 1949, "978-0451524935", "антиутопия", 328),
            Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "978-5170878521", "роман", 448),
            Book("Гарри Поттер", "Дж.К. Роулинг", 1997, "978-5389074354", "фэнтези", 432)
        ]
        save_db(db)

    while True:
        print_menu()
        choice = input("выберите действие: ")

        if choice == "1":
            if not db:
                print("база данных пуста")
            for b in db:
                print(b)

        elif choice == "2":
            title = input("название книги: ")
            author = input("автор: ")
            year = int(input("год издания: "))
            isbn = input("ISBN: ")
            genre = input("жанр: ")
            pages = int(input("количество страниц: "))
            
            db.append(Book(title, author, year, isbn, genre, pages))
            save_db(db)
            print("книга успешно добавлена")

        elif choice == "3":
            crit = input("искать по какому полю? (title/author/genre): ")
            val = input("значение для поиска: ").lower()
            results = [b for b in db if val in str(getattr(b, crit)).lower()]
            
            if not results:
                print("Ничего не найдено.")
            for r in results:
                print(r)

        elif choice == "4":
            title_search = input("введите точное название книги для изменения количества страниц: ")
            found = False
            for b in db:
                if b.title.lower() == title_search.lower():
                    b.pages = int(input("введите новое количество страниц: "))
                    save_db(db)
                    print("данные обновлены")
                    found = True
                    break
            if not found:
                print("книга с таким названием не найдена")

        elif choice == "5":
            target = input("введите название книги для удаления: ")
            found = False
            for i in range(len(db)):
                if db[i].title.lower() == target.lower():
                    delete = db.pop(i)
                    del delete 
                    save_db(db)
                    print(f"книга {target} удалена")
                    found = True
                    break
            
            if not found:
                raise ValueError(f"книга {target} не найдена в базе")

        elif choice == "6":
            field = input("поле для сортировки (title/author/year/isbn/genre/pages): ")
            sort_pyz(db, field)
            print(f"база отсортирована по полю: {field}")

        elif choice == "7":
            with open("books_export.csv", "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Название", "Автор", "Год издания", "ISBN", "Жанр", "Страницы"])
                for b in db:
                    writer.writerow([b.title, b.author, b.year, b.isbn, b.genre, b.pages])
            print("данные успешно экспортированы в файл books_export.csv")

        elif choice == "0":
            save_db(db)
            print("работа завершена")
            break
            
        else:
            print("неверный ввод, попробуйте еще раз")

if __name__ == "__main__":
    main()