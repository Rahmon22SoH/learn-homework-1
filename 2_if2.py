"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
first_line = 'work python python python'
second_line = 'moscow learn python'
def determine_age(str1, str2):
    if type(str1 and str2) != str:
        print(0)
    if str1 != str2 and " learn " in (" " + str2 + " "):
        print(3)
    if str1 != str2 and len(str1) > len(str2):
        print(2)
    elif str1 == str2:
        print(1)

determine = determine_age(first_line, second_line)
determine2 = determine_age( 0 , 'learn python')
print(determine)
print(determine2)


