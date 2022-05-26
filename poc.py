# def decor(func):
#     def wrapper():
#         print("Текущая информация:\n", )
#         func()
#     return wrapper()

class Records:  # Записи
    def __init__(self, title, deadline=None, group=None, importance=None, text=None, done=False):
        self.title = title
        self.deadline = deadline
        self.group = group
        self.importance = importance
        self.text = text
        self.done = done

    # def __init__(self, title):
    #     self.title = title
    #     self.deadline = None
    #     self.group = None
    #     self.importance = None
    #     self.text = None
    #     self.done = False

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

def print_records(dict_):
    print("---ВВЕДИТЕ НАЗВАНИЕ ЗАПИСИ, чтобы отредактировать её поля---"
          "\n(/c - вернуться в меню)")
    for val in dict_.values():
        print(f'"{val.title}"', end=" ")
    # return input("\n>> ")
    temp_ = input("\n>> ")
    for val in dict_.values():
        if temp_ == val.title:
            return val
        elif temp_ == "/c":
            return False
    print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННУЮ ЗАПИСЬ!!!\n")
    return print_records(dict_)


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
              "\t6: Поиск записей\n"
              "\t0: Выйти")  # Меню
        check = input("<---{ВВЕДИТЕ ЦИФРУ, соответствующую пункту меню}--->\n>> ")
        if check == "0":  # Выйти
            print("!___[ПРОГРАММА ЗАКРЫТА]___!")
            break

        elif check == "1":  # Добавить запись
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
                             "\t4. НеВажное НеСрочное\n>> ")  # Степень важности записи
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

        elif check == "2":  # Редактировать запись
            if records:
                record = print_records(records)
                if record is False:
                    continue
                while True:
                    print("Поля записи:\n"
                          "\t1. Название\n"
                          "\t2. Дедлайн\n"
                          "\t3. Група\n"
                          "\t4. Степень важности записи\n"
                          "\t5. Текст записи\n"
                          "\t6. Готово/Не готово")  # Поля записи
                    temp = input("<---{ВВЕДИТЕ ЦИФРУ, соответствующую полю записи}--->"
                                 "\n(0 - вернуться в меню)\n>> ")
                    if temp == "0":
                        break
                    elif temp == "1":
                        record.show_title()
                        new = input("(/c - отменить изменение поля)\n>> ")
                        record.title = new if new != "/c" else record.title
                    elif temp == "2":
                        record.show_deadline()
                        new = input("(/c - отменить изменение поля)\n>> ")
                        record.deadline = new if new != "/c" else record.deadline
                    elif temp == "3":
                        record.show_group()
                        new = input("(/c - отменить изменение поля)\n>> ")
                        record.group = new if new != "/c" else record.group
                    elif temp == "4":
                        record.show_importance()
                        new = input("Доступные степени важности записи:\n"
                                    "\t1. Важное Срочное\n"
                                    "\t2. Важное НеСрочное\n"
                                    "\t3. НеВажное Срочное\n"
                                    "\t4. НеВажное НеСрочное\n"
                                    "(/c - отменить изменение поля)\n>> ")
                        if new != "/c":
                            if new == "1":
                                record.importance = "Важное Срочное"
                            elif new == "2":
                                record.importance = "Важное НеСрочное"
                            elif new == "3":
                                record.importance = "НеВажное Срочное"
                            elif new == "4":
                                record.importance = "НеВажное НеСрочное"
                            else:
                                print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n")
                    elif temp == "5":
                        record.show_text()
                        new = input("(/c - отменить изменение поля)\n>> ")
                        record.text = new if new != "/c" else record.text
                    elif temp == "6":
                        record.show_done()
                        new = input("(/c - отменить изменение поля)\n>> ")
                        if new != "/c":
                            if new.lower() in ["1", "готово", "да", "выполнено", "true"]:
                                record.done = True
                            elif new.lower() in ["0", "не готово", "нет", "не выполнено", "false"]:
                                record.done = False
                            else:
                                print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n")
                    else:
                        print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n")
                    # break
            else:
                print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")

        elif check == "3":  # Дублировать запись
            if records:
                record = print_records(records)
                if record is False:
                    continue
                count += 1
                records[count] = record
            else:
                print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")

        elif check == "4":  # Удалить запись
            if records:
                continue
            else:
                print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")

        elif check == "5":  # Посмотреть записи
            if records:
                print("\n[ВСЕ ЗАПИСИ]:")
                for key, value in records.items():
                    print(f"\t{key}: {value.get_attrs()}")
            else:
                print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")

        elif check == "6":  # Поиск записей
            if records:
                continue
            else:
                print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")

        else:
            print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!\n"
                  "\t!Повторите ввод!")
