"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
def hello_user():
  while True:
    user_sey = input('Как дела? ')
    if user_sey == 'Хорошо':
      print(user_sey)
      break
print(hello_user())

    

    
