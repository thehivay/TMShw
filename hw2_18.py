'''task 2_18
Дается словарь с данными по успеваемости учеников. Ключи - имена, значения - лист оценок. Сформировать лист, внутри которого будут лежать кортежи (tuple) по два элемента - имя и средний балл в формате float. Кортежи внутри листа должны быть отсортированы по среднему баллу по убыванию. Если хоть у одного ученика в изначальном словаре есть оценка больше 10 или меньше 0 - вызвать ValueError. Если хоть у одного ученика в листе оценок лежит не число формата int - вызвать TypeError. Если средний балл какого-нибудь ученика < 4, то исключить его из итогового списка.
Пример: {‘aaa’: [1, 2, 7, 9, 10], ‘bbb’: [1, 2, 3, 4], ‘ccc’: [8, 9, 10]} ->
-> [(‘ccc’, 9.0), (‘aaa’, 5.8)]
Формат: dict -> list'''

d1 = {'Petya': [3, 4, 5, 6], 'Ivan': [1, 2, 3, 4, 4], 'Sveta': [8, 4, 9, 10]}


def task2_18(d1):

    l1 = []
    for imya in d1:
        oc = d1[imya]
        # print(oc)            # Вывожу значение(список оценок) по ключу(имя)
        summa = 0
        n = 0
        for ocenka in oc:
            if not isinstance(ocenka, int):
                raise TypeError('Неверный тип оценки. Должен быть int', ocenka)
            if 10 < ocenka or ocenka < 0:
                raise ValueError('Оценка не может быть < 0 и/или > 10', ocenka)
            summa = summa + ocenka
            n = n + 1
        sred = summa/n
        # print(sred)         # Средний бал

        # Отбираю средний больше 4
        if sred >= 4:
            a1 = (imya, sred)   # Создание кортежа
            # print(a1)

            # Сортировка по убыванию
            j = 0
            for m in l1:
                if sred < m[1]:
                    j += 1
            l1.insert(j, a1)

    return l1


print(task2_18(d1))
