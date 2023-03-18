from pprint import pprint
import os
with open('cook_book.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        name_of_dish = line.strip()
        count_of_ingredients = int(file.readline())
        ingredients = []
        for _ in range(count_of_ingredients):
            ingredient, ing_quantity, units_of_measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient,
                'quantity': ing_quantity,
                'measure': units_of_measure
            })
        file.readline()
        cook_book[name_of_dish] = ingredients

# print(f'Homework N#1 ------------------------------------------------------------------------------')
# pprint(cook_book, sort_dicts=False)
# print(f'Homework N#2 ------------------------------------------------------------------------------')

# print([i for i in cook_book])
def get_shop_list_by_dishes(dishes, person_count):
    new_lst = [cook_book[name_dish] for name_dish in cook_book if name_dish in dishes]
    for second_lst in new_lst:
        for dict_in_main_lst in second_lst:
            dict_in_main_lst['quantity'] = int(dict_in_main_lst['quantity']) * person_count
            print(dict_in_main_lst)

get_shop_list_by_dishes([dish for dish in input().split()], int(input()))


