from typing import TypeAlias

T_NAME: TypeAlias = str
T_OBJCTS: TypeAlias = dict
T_MENU: TypeAlias = dict


def cancel():
    return "(/c - отменить изменение поля)\n>> "


def _decor(func):
    def wrapper(*args):
        func(*args)
        return input(cancel())

    return wrapper


class Records:  # Записи
    def __init__(self, title, deadline=None, group=None, importance=None, text=None, done=False):
        self.title = title
        self.deadline = deadline
        self.group = group
        self.importance = importance
        self.text = text
        self.done = done

        self.degrees = {
            "1": "Важное Срочное",
            "2": "Важное НеСрочное",
            "3": "НеВажное Срочное",
            "4": "НеВажное НеСрочное"
        }

    # @classmethod
    # def init(cls):
    #     pass

    def set_attrs(self):
        print("<---{ЗАПОЛНИТЕ ПОЛЯ}--->\n"
              "(Enter для пропуска)\n")
        temp = input("Название записи:\n>> ")
        self.title = temp if temp != "" else self.title

        temp = input("Дедлайн (Если это задача):\n>> ")
        self.deadline = temp if temp != "" else None

        temp = input("Група записей:\n>> ")
        self.group = temp if temp != "" else None

        while True:
            print("Степень важности записи:")
            for k, v in self.degrees.items():
                print(f"\t{k}. {v}")
            temp = input(">> ")
            if temp in list(self.degrees.keys()):
                self.importance = self.degrees[temp]
            elif temp != "":
                error_with("symbol")
                print("\t!Повторите ввод!")
                continue
            break

        temp = input("Текст записи:\n>> ")
        self.text = temp if temp != "" else None

    def get_attrs(self) -> tuple:
        return self.title, self.deadline, self.group, self.importance, self.text, self.done

    @_decor
    def show_title(self):
        print(f"Название записи: {self.title}")

    @_decor
    def show_deadline(self):
        if self.deadline is None:
            print(f'Дедлайн записи "{self.title}" не установлен.')
        else:
            print(f'Дедлайн записи "{self.title}": {self.deadline}')

    @_decor
    def show_group(self):
        if self.group is None:
            print(f'Запись "{self.title}" не принадлежит ни к какой группе.')
        else:
            print(f'Запись "{self.title}" принадлежит к группе "{self.group}".')

    @_decor
    def show_importance(self):
        if self.importance is None:
            print(f'Запись "{self.title}" не имеет степеня важности.')
        else:
            print(f'Запись "{self.title}" имеет степень важности "{self.importance}"')
        print("Доступные степени важности записи:\n"
              "\t1. Важное Срочное\n"
              "\t2. Важное НеСрочное\n"
              "\t3. НеВажное Срочное\n"
              "\t4. НеВажное НеСрочное")

    @_decor
    def show_text(self):
        if self.text is None:
            print(f'Запись "{self.title}" не имеет описания.')
        else:
            print(f'Описание записи "{self.title}":\n"{self.text}"')

    @_decor
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


def menu() -> str:
    menu_item_names = {
        "1": "Добавить запись",
        "2": "Редактировать запись",
        "3": "Дублировать запись",
        "4": "Удалить запись",
        "5": "Посмотреть записи",
        "6": "Поиск записей",
        "0": "Выйти"
    }
    print("\nМеню приложения:")
    for k, v in menu_item_names.items():
        print(f"\t{k}: {v}")
    return input("<---{ВВЕДИТЕ ЦИФРУ, соответствующую пункту меню}--->\n>> ")


def error_with(which_error):
    if which_error == "symbol":
        return print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННЫЙ СИМВОЛ!!!")
    elif which_error == "record":
        return print("!!!ВЫ ВВЕЛИ НЕЗАРЕГИСТРИРОВАННУЮ ЗАПИСЬ!!!")
    elif which_error == "empty":
        return print("<---{СПИСОК ЗАПИСЕЙ ПУСТ}--->")


def check_by_title(dict_: T_OBJCTS) -> (tuple,):
    for val in dict_.values():
        print(f'"{val.title}"', end=" ")
    temp_ = input("\n>> ")
    for k, val in dict_.items():
        if temp_ == val.title:
            return k, val
        elif temp_ == "/c":
            return k, False
    error_with("record")
    return check_by_title(dict_)


def show_records(recs: T_OBJCTS):
    print("\n[ВСЕ ЗАПИСИ]:")
    for key, value in recs.items():
        print(f"\t{key}: {value.get_attrs()}")


def choose_field() -> str:
    print("Поля записи:")
    record_fields = {
        "1": "Название",
        "2": "Дедлайн",
        "3": "Група",
        "4": "Степень важности записи",
        "5": "Текст записи",
        "6": "Готово/Не готово"
    }
    for key, value in record_fields.items():
        print(f"\t{key}: {value}")
    return input("<---{ВВЕДИТЕ ЦИФРУ, соответствующую полю записи}--->"
                 "\n(0 - вернуться в меню)\n>> ")


def p_0(recs: dict, c: int):
    print("!___[ПРОГРАММА ЗАКРЫТА]___!")
    return False, recs, c


def p_1(recs: dict, c: int):
    c += 1
    obj = Records(f"Запись №{c}")
    obj.set_attrs()
    recs[c] = obj
    return True, recs, c


def p_2(recs: dict, c: int):
    def p_2_1(rec):
        new = rec.show_title()
        rec.title = new if new != "/c" else rec.title

    def p_2_2(rec):
        new = rec.show_deadline()
        rec.deadline = new if new != "/c" else rec.deadline

    def p_2_3(rec):
        new = rec.show_group()
        rec.group = new if new != "/c" else rec.group

    def p_2_4(rec):
        new = rec.show_importance()
        if new != "/c":
            if new in list(rec.degrees.keys()):
                rec.importance = rec.degrees[new]
            else:
                error_with("symbol")

    def p_2_5(rec):
        new = rec.show_text()
        rec.text = new if new != "/c" else rec.text

    def p_2_6(rec):
        new = rec.show_done()
        if new != "/c":
            if new.lower() in ["1", "готово", "да", "выполнено", "true"]:
                rec.done = True
            elif new.lower() in ["0", "не готово", "нет", "не выполнено", "false"]:
                rec.done = False
            else:
                error_with("symbol")

    if recs:
        print("---ВВЕДИТЕ НАЗВАНИЕ ЗАПИСИ, чтобы ОТРЕДАКТИРОВАТЬ её поля---"
              "\n(/c - вернуться в меню)")
        key, record = check_by_title(recs)
        if record is False:
            return True, recs, c
        a = {
            "0": False,
            "1": p_2_1,
            "2": p_2_2,
            "3": p_2_3,
            "4": p_2_4,
            "5": p_2_5,
            "6": p_2_6,
        }
        while True:
            field = choose_field()
            if field == "0":
                break
            elif field in list(a.keys()):
                a[field](record)
            else:
                error_with("symbol")
    else:
        error_with("empty")
    return True, recs, c


def p_3(recs: dict, c: int):
    if recs:
        print("---ВВЕДИТЕ НАЗВАНИЕ ЗАПИСИ, которую хотите ДУБЛИРОВАТЬ---"
              "\n(/c - вернуться в меню)")
        key, record = check_by_title(recs)
        if record is False:
            return True, recs, c
        c += 1
        recs[c] = record
    else:
        error_with("empty")
    return True, recs, c


def p_4(recs: dict, c: int):
    if recs:
        print("---ВВЕДИТЕ НАЗВАНИЕ ЗАПИСИ, которую хотите УДАЛИТЬ---"
              "\n(/c - вернуться в меню)")
        key, record = check_by_title(recs)
        if record is False:
            return True, recs, c
        c -= 1
        recs.pop(key)
        return True, recs, c
    else:
        error_with("empty")
    return True, recs, c


def p_5(recs: dict, c: int):
    if recs:
        show_records(recs)
    else:
        error_with("empty")
    return True, recs, c


def p_6(recs: dict, c: int):
    if recs:
        record = input("---ВВЕДИТЕ НАЗВАНИЕ ЗАПИСИ, информацию о которой хотите НАЙТИ---"
                       "\n(/c - вернуться в меню)\n>> ")
        if record == "/c":
            return True, recs, c
        for v in recs.values():
            if v.get_attrs()[0] == record:
                for i in v.get_attrs():
                    print(i, end=", ")
                print("")
                return True, recs, c
        print("Запись с таким названием НЕ была найдена!")
    else:
        error_with("empty")
    return True, recs, c


if __name__ == "__main__":
    records = {}
    count = 0
    menu_items = {
        "0": p_0,
        "1": p_1,
        "2": p_2,
        "3": p_3,
        "4": p_4,
        "5": p_5,
        "6": p_6
    }
    while True:
        point = menu()
        if point in list(menu_items.keys()):
            res, records, count = menu_items[point](records, count)
        else:
            error_with("symbol")
            print("\t!Повторите ввод!")
            continue
        if res is False:
            break
