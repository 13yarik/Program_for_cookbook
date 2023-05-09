import json

def load_cookbook(file_name):
    cook_book = {}
    with open(file_name, "r", encoding="utf-8") as f: 
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
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = load_cookbook('cookbook.txt')
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' не найдено в книге рецептов")
            continue
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            ingredient['quantity'] *= person_count
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
            else:
                shop_list[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'], 'measure': ingredient['measure']}
    return shop_list

cookbook = load_cookbook("cookbook.txt")
# print(json.dumps(cookbook, indent=2, ensure_ascii=False)) 

shop = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
# print(json.dumps(shop, indent=2, ensure_ascii=False)) 



