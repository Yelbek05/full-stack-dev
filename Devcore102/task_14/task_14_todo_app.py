from datetime import datetime

class Todo:
    def __init__(self, id, description, deadline):
        self.id = id
        self.description = description
        self.is_completed = False
        self.deadline = deadline
        
    def __str__(self):
        return f"{self.id}, {self.description} — Выполнение задач: {self.is_completed}, Дата выполнения: {self.deadline}"

class DoList:
    def __init__(self):
        self.tasks = {}
        for id, description, deadline in self.get_dict_for_tasks():
            task = Todo(id, description, deadline)
            self.tasks[id] = task

    def get_dict_for_tasks(self):
        return [
            (1, "Принят душ", "2021-09-30"),
            (2, "Пить 1 стакан воды", "2021-02-10"),
            (3, "Выключит компютер", "2021-09-30"),
            (4, "проходить module(Devcore105)", "2021-01-30"),
            (5, "есть ужин", "2021-03-30"),
            (6, "читать 1 chapter книги", "2021-10-30"),
            (7, "Ложиться спать", "2021-06-30")
        ]
    def display_tasks(self):
        for id, description in self.tasks.items():
            print(f"{description}")

    def add_task(self):
        try:
            id = int(input("Введите id задачи: "))
            description = input("Введите описание задачи: ")
            deadline = input("Введите дату выполнения задачи: ")
            task = Todo(id, description, deadline)
            self.tasks[id] = task
            print(f"Задача '{description}' добавлена в список.")
            self.display_tasks()
        except ValueError:
            print("Некорректный ввод, введите число.")

    def delete_task(self):
        id = int(input("Введите id задачи для удаление: "))
        if id in self.tasks:
            del self.tasks[id]
            print(f"Задача с id {id} удалена.")
        else:
            print(f"Задача с id {id} не найдена.")
    
    def mark_task_as_completed(self):
        id = int(input("Введите id задачи для пометки как выполненной:"))
        if id in self.tasks:
            self.tasks[id].is_completed = True
            print(f"Задача с id {id} помечена как выполненная.")
        else:
            print(f"Задача с id {id} не найдена.")
    
    def save_tasks_to_file(self):
        directory = '/home/abstract/full-stack-dev/Devcore102/task_14/task_14.txt'
        with open(directory, "w") as file:
            for id, desc in self.tasks.items():
                file.write(f"{id}, {desc.description}, {desc.is_completed}, {desc.deadline}\n")
        print("Задачи сохранены в файл.")
    
    def load_tasks_from_file(self):
        directory = '/home/abstract/full-stack-dev/Devcore102/task_14/task_14.txt'
        with open(directory, "r") as file:
            for line in file:
                id, description, is_completed, deadline = line.strip().split(", ")
                task = Todo(int(id), description, deadline)
                task.is_completed = is_completed == "True"
                self.tasks[int(id)] = task
            print("Задачи загружены из файла.")

    def add_task_with_deadline(self):
        try:
            id = int(input("Введите id задачи: "))
            description = input("Введите описание задачи: ")
            deadline = input("Введите дату выполнения задачи: ")
            task = Todo(id, description, deadline)
            self.tasks[id] = task
            print(f"Задача '{description}' добавлена в список.")
            self.display_tasks()
        except ValueError:
            print("Некорректный ввод, введите число.")

    def sort_tasks_by_date(self):
        sorted_tasks = sorted(self.tasks.values(), key=lambda task: datetime.strptime(task.deadline, "%Y-%m-%d"))
        for task in sorted_tasks:
            print(task)

def main():
    do_list = DoList()

    do_list.display_tasks()

    while True:
        print("\nВыберите действию")
        print("1. добавить новую задачу.")
        print("2. удалить задачу.")
        print("3. показать все задачи.")
        print("4. пометить задачу как выполненную.")
        print("5. завершить выполнение программы.")
        print("6. сохранять задачи в файл")
        print("7. загрузить задачи из файла")
        print("8. добавлять задачи с установленными сроками выполнения")
        print("9. сортировать задачи по дате")
        choice = input("Вводите действию: ")

        if choice == "1":
            do_list.add_task()

        elif choice == "2":
            do_list.delete_task()

        elif choice == "3":
            do_list.display_tasks()
        
        elif choice == "4":
            do_list.mark_task_as_completed()
        
        elif choice == "5":
            break
        
        elif choice == "6":
            do_list.save_tasks_to_file()

        elif choice == "7":
            do_list.load_tasks_from_file()

        elif choice == "8":
            do_list.add_task_with_deadline()

        elif choice == "9":
            do_list.sort_tasks_by_date()

if __name__ == '__main__':
    main()