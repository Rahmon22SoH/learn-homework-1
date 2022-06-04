

def discounted(price, discount, max_discound=20):
    
    try:
        price = float(price)
        discount = float(discount)
        max_discound = int(max_discound)
        if max_discound >= 20:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discound:
            raise TypeError ("Больше максимальной скидки")
        if price - (price * discount / 20):
            raise ZeroDivisionError ("Ошибка типа или нельзя делить на 0")            
    except ZeroDivisionError:
        print('Не надо делить на ноль')
    except ValueError:
        print('Ошибка ValueError в Python')
    except TypeError:
        print("Ошибка типа")
     


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100.5", "4.5","5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
