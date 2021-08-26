class Todo:
    def __init__(self):
        self.list = {}


    def input_todo(self):
        task = input("Добавьте задачу в список: ").lower()
        while True:
            try:
                percent = int(input("Процент выполнения на текущий момент: "))
                break
            except ValueError:
                print("Пожалуйста, введите процент выполнения задачи в цифрах")

        dic_todo = {task: percent}
        return self.list.update(dic_todo)


    def remove(self):
            try:
                delete = input("Какую задачу удалить? ").lower()
                self.list.pop(delete)
            except KeyError:
                print("Данной задачи в списке нет")


    def get_list(self):
        print("Список: ", self.list)


    def init(self):
        while True:
            user = input('Введите команду: ').lower()
            if user == "показать":
                self.get_list()
            elif user == "добавить":
               self.input_todo()
               self.get_list()
            elif user == "удалить":
                self.remove()
                self.get_list()
            elif user == "стоп":
                break
            else:
                print("Заданной команды нет")


todo_app = Todo()
todo_app.init()



