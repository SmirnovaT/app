class Todo:
    def __init__(self):
        self.items = []

    def input_todo(self):
        task = input("Добавьте задачу в список: ").lower()
        while True:
            try:
                percent = int(input("Введите процент выполнения задачи: "))
                break
            except ValueError:
                print("Пожалуйста, введите процент выполнения в цифрах")

        sum = f"{task}: {percent}"
        return self.items.append(sum)


    def remove(self):
        delete = input("Что удалить из списка: ").lower()
        for el in self.items:
            if delete in el:
                self.items.remove(el)
            else:
                print("Данной задачи в списке нет")

    def get_list(self):
       print("Список: ", self.items)


    def init(self):
        while True:
            user = input("Введите команду: ").lower()
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
                print("Заданной команды нет, повторите ввод")


todo_app = Todo()
todo_app.init()