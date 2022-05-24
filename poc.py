# def decor(func):
#     def wrapper():
#         print("Текущая информация:\n", )
#         func()
#     return wrapper()

class Records:  # Записи
    # def init(self, title, deadline=None, group=None, importance=None, text=None, done=False):
    #     self.title = title
    #     self.deadline = deadline
    #     self.group = group
    #     self.importance = importance
    #     self.text = text
    #     self.done = done
    def __init__(self, title):
        self.title = title
        self.deadline = None
        self.group = None
        self.importance = None
        self.text = None
        self.done = False

    def get_attrs(self):
        return self.title, self.deadline, self.group, self.importance, self.text, self.done

    def show_title(self):
        print(f"Название записи: {self.title}")

    def show_deadline(self):
        if self.deadline is None:
            print(f'Дедлайн записи "{self.title}" не установлен.')
        else:
            print(f'Дедлайн записи "{self.title}": {self.deadline}')

    def show_group(self):
        if self.group is None:
            print(f'Запись "{self.title}" не принадлежит ни к какой группе.')
        else:
            print(f'Запись "{self.title}" принадлежит к группе "{self.group}".')

    def show_importance(self):
        if self.importance is None:
            print(f'Запись "{self.title}" не имеет степеня важности.')
        else:
            print(f'Запись "{self.title}" имеет степень важности "{self.importance}"')

    def show_text(self):
        if self.text is None:
            print(f'Запись "{self.title}" не имеет описания.')
        else:
            print(f'Описание записи "{self.title}":\n"{self.text}"')

    def show_done(self):
        if self.done:
            print(f'Запись "{self.title}" выполнена.')
        else:
            print(f'Запись "{self.title}" не выполнена.')


# class TaskManager(Records):  # Задачи
#     def __init__(self, title):
#         super().__init__(title)
#
#
# class Notes(Records):  # Заметки
#     def __init__(self, title):
#         super().__init__(title)


if __name__ == "__main__":
    records = {}
    count = 0
    while True:
        print("\nМеню приложения:\n"
              "\t1: Добавить запись\n"
              "\t2: Редактировать запись\n"
              "\t3: Дублировать запись\n"
              "\t4: Удалить запись\n"
              "\t5: Посмотреть записи\n"
              "\t0: Выйти")
        check = input("<---{ВВЕДИТЕ ЦИФРУ, соответствующую пункту меню}--->\n>> ")
        if check == "0":
            break

        elif check == "1":
            count += 1
            obj = Records(f"Запись №{count}")
            temp = input("<---{ЗАПОЛНИТЕ ПОЛЯ}--->\n"
                         "(Enter для пропуска)\n"
                         "\nНазвание записи:\n>> ")
            if temp != "":
                obj.title = temp

            temp = input("Дедлайн задачи:\n>> ")
            if temp != "":
                obj.deadline = temp

            temp = input("Група записей:\n>> ")
            if temp != "":
                obj.group = temp

            while True:
                temp = input("Степень важности записи:\n"
                             "\t1. Важное Срочное\n"
                             "\t2. Важное НеСрочное\n"
                             "\t3. НеВажное Срочное\n"
                             "\t4. НеВажное НеСрочное\n>> ")
                if temp == "":
                    break
                elif temp == "1":
                    obj.importance = "Важное Срочное"
                elif temp == "2":
                    obj.importance = "Важное НеСрочное"
                elif temp == "3":
                    obj.importance = "НеВажное Срочное"
                elif temp == "4":
                    obj.importance = "НеВажное НеСрочное"
                else:
                    print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n"
                          "\t!Повторите ввод!")
                    continue
                break

            temp = input("Текст записи:\n>> ")
            if temp != "":
                obj.text = temp

            records[count] = obj
        elif check == "2":
            if records:
                print("---ВВЕДИТЕ НАЗВАНИЕ ЗАПИСИ, чтобы отредактировать её поля---")
                for value in records.values():
                    print(f'"{value.title}"', end=" ")
                temp = input("\n>> ")
                for value in records.values():
                    if temp == value.title:
                        while True:
                            print("Поля записи:\n"
                                  "\t1. Название\n"
                                  "\t2. Дедлайн\n"
                                  "\t3. Група\n"
                                  "\t4. Степень важности записи\n"
                                  "\t5. Текст записи\n"
                                  "\t6. Готово/Не готово")
                            temp = input("<---{ВВЕДИТЕ ЦИФРУ, соответствующую полю записи}--->\n"
                                         "(0 - вернуться в меню)\n>> ")
                            if temp == "0":
                                break
                            elif temp == "1":
                                value.show_title()
                                print("(/c - отменить изменение поля)")
                                new = input(">> ")
                                if new != "/c":
                                    value.title = new
                            elif temp == "2":
                                value.show_deadline()
                                print("(/c - отменить изменение поля)")
                                new = input(">> ")
                                if new != "/c":
                                    value.deadline = new
                            elif temp == "3":
                                value.show_group()
                                print("(/c - отменить изменение поля)")
                                new = input(">> ")
                                if new != "/c":
                                    value.group = new
                            elif temp == "4":
                                value.show_importance()
                                print("(/c - отменить изменение поля)")
                                new = input("Доступные степени важности записи:\n"
                                            "\t1. Важное Срочное\n"
                                            "\t2. Важное НеСрочное\n"
                                            "\t3. НеВажное Срочное\n"
                                            "\t4. НеВажное НеСрочное\n>> ")
                                if new != "/c":
                                    if new == "1":
                                        value.importance = "Важное Срочное"
                                    elif new == "2":
                                        value.importance = "Важное НеСрочное"
                                    elif new == "3":
                                        value.importance = "НеВажное Срочное"
                                    elif new == "4":
                                        value.importance = "НеВажное НеСрочное"
                                    else:
                                        print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n")
                            elif temp == "5":
                                value.show_text()
                                print("(/c - отменить изменение поля)")
                                new = input(">> ")
                                if new != "/c":
                                    value.text = new
                            elif temp == "6":
                                value.show_done()
                                print("(/c - отменить изменение поля)")
                                new = input(">> ")
                                if new != "/c":
                                    if new.lower() in ["1", "готово", "да", "выполнено", "true"]:
                                        value.done = True
                                    elif new.lower() in ["0", "не готово", "нет", "не выполнено", "false"]:
                                        value.done = False
                                    else:
                                        print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n")
                            else:
                                print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n")
                        break
                    else:
                        print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")

        elif check == "5":
            if records:
                print("\n[ВСЕ ЗАПИСИ]:")
                for key, value in records.items():
                    print(f"\t{key}: {value.get_attrs()}")
            else:
                print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")

        else:
            print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n"
                  "\t!Повторите ввод!")
