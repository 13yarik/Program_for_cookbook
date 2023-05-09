import json

cook_book = {}
with open("cookbook.txt", "r", encoding="utf-8") as f: # encoding добавил т.к почему-то выдает ошибку кодировки, при которой невозможна декодировка байтовых данных, хотя текстовый файл создавал в нормальной кодировке utf-8
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        ingredients_count = int(f.readline().strip())
        ingredients_list = []
        for i in range(ingredients_count):
            ingredient_data = f.readline().strip().split('|')
            ingredient_name = ingredient_data[0].strip()
            quantity = int(ingredient_data[1].strip())
            measure = ingredient_data[2].strip()
            ingredient_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            ingredients_list.append(ingredient_dict)
            cook_book[dish_name] = ingredients_list
    print(json.dumps(cook_book, indent=2, ensure_ascii=False)) # Для красивого вывода (indent = отступы для каждого уровня вложенности)
                                                               #                      (ensure_ascii=False - чтобы отобразить русские буквы)




