import csv
from planet import Planet, load_db, save_db, sort_pyz

def print_menu():
    print("\nМЕНЮ БАЗЫ ДАННЫХ ПЛАНЕТ")
    print("1 просмотр всех записей")
    print("2 добавление планеты")
    print("3 поиск планеты")
    print("4 редактирование (изменение радиуса)")
    print("5 удаление планеты")
    print("6 сортировка")
    print("7 экспорт в CSV")
    print("0 выход")

def main():
    db = load_db()
    
    
    if not db:
        db = [
            Planet("Марс", 3389, 6.39e23, 227.9, "каменная"),
            Planet("Юпитер", 69911, 1.89e27, 778.5, "газовый гигант"),
            Planet("Земля", 6371, 5.97e24, 149.6, "каменная")
        ]


    while True:
        print_menu()
        choice = input("выберите действие: ")

        if choice == "1":
            if not db:
                print("база данных пуста")
            for p in db:
                print(p)

        elif choice == "2":
            name = input("название планеты: ")
            radius = int(input("радиус: "))
            mass = float(input("масса: "))
            distance = float(input("расстояние от Солнца: "))
            p_type = input("тип планеты: ")
            
            db.append(Planet(name, radius, mass, distance, p_type))
            save_db(db)
            print("планета успешно добавлена")

        elif choice == "3":
            crit = input("искать по какому полю? (name/p_type): ")
            val = input("значение для поиска: ").lower()
            results = [p for p in db if val in str(getattr(p, crit)).lower()]
            
            if not results:
                print("Ничего не найдено.")
            for r in results:
                print(r)

        elif choice == "4":
            name = input("введите точное название планеты для изменения радиуса: ")
            found = False
            for p in db:
                if p.name.lower() == name.lower():
                    p.radius = int(input("введите новый радиус: "))
                    save_db(db)
                    print("данные обновлены")
                    found = True
                    break
            if not found:
                print("планета с таким названием не найдена")

        elif choice == "5":
            target = input("введите название планеты для удаления: ")
            found = False
            for i in range(len(db)):
                if db[i].name.lower() == target.lower():
                    delete = db.pop(i)
                    del delete  
                    save_db(db)
                    print(f"планета {target} удалена")
                    found = True
                    break
            
            if not found:
                raise ValueError(f"планета {target} не найдена в базе")

        elif choice == "6":
            field = input("поле для сортировки (name/distance/radius/mass/p_type): ")
            sort_pyz(db, field)
            print(f"база отсортирована по полю: {field}")

        elif choice == "7":
            with open("planets_export.csv", "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Название", "Радиус (км)", "Масса (кг)", "Расстояние (млн км)", "Тип"])
                for p in db:
                    writer.writerow([p.name, p.radius, p.mass, p.distance, p.p_type])
            print("данные успешно экспортированы в файл planets_export.csv")

        elif choice == "0":
            save_db(db)
            print("работа завершена")
            break
            
        else:
            print("неверный ввод, попробуйте еще раз")

if __name__ == "__main__":
    main()