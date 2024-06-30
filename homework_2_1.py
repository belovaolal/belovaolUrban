"""
На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:
Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0

Пример результата выполнения программы:
Ввод в консоль 1:
123
456
789

Вывод на консоль 1:
0

Ввод в консоль 2:
42
69
42

Вывод на консоль 2:
2

Примечания:
Помните, что условная конструкция начинается с if.
Операторы elif и else не могут существовать самостоятельно, они являются продолжением условной конструкции.
Старайтесь избегать вложенности условий и описывать их, используя операторы or, and и not.
Самое хорошее решение не только самое быстрое, но ещё и хорошо читаемое!
Файл с кодом (module_2_2.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.
"""

first = int(input('введите первое число: '))
second = int(input('введите второе число: '))
third = int(input('введите третье число: '))
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

