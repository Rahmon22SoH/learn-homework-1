"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара +
* Посчитать и вывести среднее количество продаж для каждого товара +
* Посчитать и вывести суммарное количество продаж всех товаров  
* Посчитать и вывести среднее количество продаж всех товаров
"""
# Не могу посчитать и вывести суммарное количество продаж всех товаров -
# Не могу посчитать и вывести среднее количество продаж всех товаров -

stok = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def calculation_statistics_avg(lists):
    avg_product = 0
    for sum_sale in lists:
      avg_product += sum_sale
    return avg_product  / len(lists)
    
def calculation_statistics(sum_avg):
    stat_product = 0
    for sum_sale in sum_avg:
        stat_product += sum_sale
    return stat_product

       
avg_sum = 0     
for sum_sales in stok:
    phone_sum = calculation_statistics_avg(sum_sales['items_sold'])
    print(f"среднее количество продаж для каждого товара : {round(phone_sum)}")
    avg_sum += phone_sum
    
 
product_sum = 0
for all_sales in stok:
    phone_sum = calculation_statistics(all_sales['items_sold'])
    print(f"Суммарное количество продаж для каждого товара {phone_sum}")
  
