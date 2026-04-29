class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        student = Student(name, grade)
        self.students.append(student)
        print(f"Студента {name} успішно додано.")

    def show_list(self):
        for i in range(len(self.students)):
            print(f"{i+1}> {self.students[i].name} {self.students[i].grade}")
            
    def check_status(self):
        if not self.students:
            print("Список порожній")
            return
            
        for student in self.students:
            if student.grade >= 60:
                print(f"{student.name}: бюджет")
            else:
                print(f"{student.name}: контракт")
        
    def show_statistics(self):
        if not self.students:
            print("Список порожній. Статистика недоступна")
            return
            
        total_grade = 0
        for student in self.students:
            total_grade += student.grade
                
        average = total_grade / len(self.students)
        print(f"Середній бал: {average:.2f}")

manager = StudentManager()

while True:
    print("Меню менеджер студентів")
    print("1. Додати")
    print("2. Показати список")
    print("3. Перевірити статус (бюджет/контракт)")
    print("4. Показати статистику")
    print("0. Вийти")
    
    action = input("Оберіть дію: 0-4\n")
     
    while action not in ["0", "1", "2", "3", "4"]:
        print("Невірний вибір. Спробуйте ще раз")
        action = input("Оберіть дію (0-4):\n")
         
    if action == "1":
        name = input("Введіть ім'я студента:\n")
        try:
            grade = float(input("Введіть оцінку:\n"))
            manager.add_student(name, grade)
        except ValueError:
            print("Помилка: Оцінка має бути числом!") 
    elif action == "2":
        manager.show_list()
    elif action == "3":
        manager.check_status()
    elif action == "4":
        manager.show_statistics()
    elif action == "0":
        print("Роботу завершено")
        break

                    
                    
             
         
    