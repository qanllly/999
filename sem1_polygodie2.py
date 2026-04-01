class Department:
    total_departments = 0

    def __init__(self, name, head_name, staff_count):
        self.name = name
        self.head_name = head_name
        self.__staff_count = staff_count
        Department.total_departments += 1

    @property
    def staff_count(self):
        return self.__staff_count

    @staff_count.setter
    def staff_count(self, value):
        if value <= 0:
            raise ValueError("сотрудников должно быть больше нуля")
        self.__staff_count = value

    @classmethod
    def from_string(cls, data_str):
        name, head, count = data_str.split(',')
        return cls(name.strip(), head.strip(), int(count))

    def dept_info(self):
        print(f"кафедра: {self.name}, заведующий: {self.head_name}, сотрудников: {self.staff_count}")

dep1 = Department("ИУ7", "Иванов И.И.", 45)
dep2 = Department.from_string("ИУ9, Петров П.П., 30")

dep1.dept_info()
dep2.dept_info()
print("всего кафедр:", Department.total_departments)