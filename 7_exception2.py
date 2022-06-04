"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discound=20):
    
    try:
        price = float(price)
        discount = float(discount)
        max_discound = int(max_discound)
        max_discound = int(max_discound)
        if max_discound >= 20:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discound:
            raise TypeError ("Больше максимальной скидки")
        if price - (price * discount / 20):
            raise ZeroDivisionError ("Ошибка типа или нельзя делить на 0")                         

    except ValueError:
        print('функция получает аргумент  не поддерживаемого типа')
    except TypeError:
        print('функция применяется к объекту несовместимого типа')
    except ZeroDivisionError:
        print('на ноль делить не льзя')



print(discounted(100.2, 2.4))
print(discounted(100, "3"))
print(discounted("100.5", "4.5","5"))
print(discounted("five", 5))
print(discounted("сто", "десять"))
print(discounted(100.0, 5, "10"))