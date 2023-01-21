import doctest


class Student:
    def __init__(self, number_course: int, sred_ball: float):
        """
        Создание и подготовка к работе объекта "Студент"
        :param number_course: Номер курса
        :param sred_ball: Средняя оценка
        Примеры:
        >>> student = Student(2, 4.6) # инициализация экземпляра класса
        """
        if not isinstance(number_course, int):
            raise TypeError("Номер курса должен быть типа int")

        if not((number_course >= 1) and (number_course <= 6)):
            raise ValueError("Номер курса должен быть в диапазоне от 1 до 6")

        self.number_course = number_course

        if not isinstance(sred_ball, (float, int)):
            raise TypeError("Средни балл должен быть типа float/int")

        if not((sred_ball >= 2) and (sred_ball <= 5)):
            raise ValueError("Средни балл должен быть в диапазоне от 2 до 5")

        self.sred_ball = sred_ball

    def sled_course(self) -> None:
        """
        Функция которая переводит студента на следующи курс
        :raise ValueError: Если номер курса превышает 6, то ошибка
        Примеры:
        >>> student = Student(2, 4.6)
        >>> student.sled_course()
        """
        if self.number_course == 6:
            raise ValueError("Студент выпущен из ВУЗа")
        ...

    def has_stipendia(self) -> bool:
        """
        Определяет наличие стипендии по среднему баллу.
        :return: Имеет стипендию (True) / Не имеет стипендии (False)
        Примеры:
        >>> student = Student(2, 4.6)
        >>> student.has_stipendia()
        """
        ...

    if __name__ == "__main__":
        doctest.testmod() # тестирование примеров, которые находятся в документации


class Room:
    def __init__(self, param_dlina: float, param_shirina: float, param_visota: float):
        """
        Создание и подготовка к работе объекта "Комната"
        :param param_dlina: Длина комнаты
        :param param_shirina: Ширина комнаты
        :param param_visota: Высота комнаты
        Примеры:
        >>> room = Room(10, 4.6, 3.2) # инициализация экземпляра класса
        """
        if not isinstance(param_dlina, (float, int)):
            raise TypeError("Длина комнаты должна быть типа float/int")

        if not(param_dlina > 0):
            raise ValueError("Длина комнаты должна быть больше 0")

        self.param_dlina = param_dlina

        if not isinstance(param_shirina, (float, int)):
            raise TypeError("Длина комнаты должна быть типа float/int")

        if not(param_shirina > 0):
            raise ValueError("Ширина комнаты должна быть больше 0")

        self.param_shirina = param_shirina

        if not isinstance(param_visota, (float, int)):
            raise TypeError("Высота комнаты должна быть типа float/int")

        if not(param_visota > 2.2):
            raise ValueError("Высота комнаты должна быть больше 2.2")

        self.param_visota = param_visota

    def plosh_sten(self) -> float:
        """
        Функция которая определяет площадь стен
        :return: Площадь стен
        Примеры:
        >>> room = Room(10, 4.6, 3.2)
        >>> plosh = room.plosh_sten()
        """
        ...

    def proverka(self, min_ploshad: float) -> bool:
        """
        Определяет допустима ли площадь помещения
        :param min_ploshad: Минимальная площадь комнаты
        :raise ValueError: Если введено неправильное число минимально площади
        :return: Допустимо(True) / Недопустимо(False)
        Примеры:
        >>> room = Room(10, 4.6, 3.2)
        >>> plosh = room.proverka(20.1)
        """
        if not isinstance(min_ploshad, (int, float)):
            raise TypeError("Минимальная площадь должна быть типа int или float")
        if not(min_ploshad > 0):
            raise ValueError("Минимальная площадь должна быть положительным числом")
        ...

    if __name__ == "__main__":
        doctest.testmod() # тестирование примеров, которые находятся в документации


class Brigada:
    def __init__(self, number_person: int, name_brigadir: str):
        """
        Создание и подготовка к работе объекта "Бригада"
        :param number_person: Количество членов бригады
        :param name_brigadir: Фамилия бригадира
        Примеры:
        >>> brigada = Brigada(10, "Шабунина") # инициализация экземпляра класса
        """
        if not isinstance(number_person, int):
            raise TypeError("Количество членов бригады должно быть типа int")

        if not(number_person > 0):
            raise ValueError("Количество членов бригады должно быть больше 0")

        self.number_person = number_person

        if not isinstance(name_brigadir, str):
            raise TypeError("Фамилия бригадира должна быть типа str")

        self.name_brigadir = name_brigadir

    def uvolnenie(self) -> None:
        """
        Функция которая увольняет одного человека
        :raise ValueError: Если некого увольнять
        Примеры:
        >>> brigada = Brigada(10, "Шабунина")
        >>> brigada.uvolnenie()
        """
        if self.number_person == 1:
            raise ValueError("Увольнять некого")
        ...

    def zarplata(self, summ: float) -> float:
        """
        Определяет всем равную зарплату
        :param summ: Сумма зарабатка бригадо
        :raise ValueError: Если введено неправильное число
        :return: Сумма зарабатка одним человеком
        Примеры:
        >>> brigada = Brigada(10, "Шабунина")
        >>> zp = brigada.zarplata(2040152.12)
        """
        if not isinstance(summ, (int, float)):
            raise TypeError("Сумма зарабатка бригадо должна быть типа int или float")
        if not(summ > 0):
            raise ValueError("Сумма зарабатка бригадо должна быть положительным числом")
        ...

    if __name__ == "__main__":
        doctest.testmod() # тестирование примеров, которые находятся в документации

#end