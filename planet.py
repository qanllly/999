import json
import os

#класс

class Planet:
    __count = 0

    def __init__(self, name, radius, mass, distance, p_type):
        Planet.__count += 1
        self.__id = Planet.__count
        
        self.name = name
        self.radius = radius     
        self.mass = mass       
        self.distance = distance
        self.p_type = p_type 
        print(f"Создание ID {self.__id}")

    def __del__(self):
        print(f"Удаление ID {self.__id}")

    def __str__(self):
        return (f"[{self.__id}] {self.name:<10} | Тип: {self.p_type:<15} | "
                f"Радиус: {self.radius:>6} км | Расстояние: {self.distance:>8} млн км")

    def __repr__(self):
        return f"Planet('{self.name}', {self.distance})"

    def __lt__(self, other):
        if not isinstance(other, Planet):
            raise TypeError("Сравнение возможно только с объектом Planet")
        return self.distance < other.distance

    def __eq__(self, other):
        if not isinstance(other, Planet):
            return False
        return self.name.lower() == other.name.lower()

    def __copy__(self):
        return Planet(self.name, self.radius, self.mass, self.distance, self.p_type)

    def to_dict(self):
        return {
            "name": self.name, "radius": self.radius,
            "mass": self.mass, "distance": self.distance, "p_type": self.p_type
        }

#бд
DB_PATH = "planets.json"

def save_db(planets):
    data = [p.to_dict() for p in planets]
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Planet(item['name'], item['radius'], item['mass'], item['distance'], item['p_type']) for item in data]

#сорт

def sort_pyz(planets, field_name):
    n = len(planets)
    for i in range(n):
        for j in range(0, n - i - 1):
            if field_name == "distance":
                if planets[j+1] < planets[j]:
                    planets[j], planets[j+1] = planets[j+1], planets[j]
            else:
                val1 = getattr(planets[j], field_name)
                val2 = getattr(planets[j+1], field_name)
                if val1 > val2:
                    planets[j], planets[j+1] = planets[j+1], planets[j]