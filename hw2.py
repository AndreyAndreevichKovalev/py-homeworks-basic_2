from pprint import pprint


def read_cook_book(file_path: str) -> dict[str, list]:
    cook_book: dict = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name: str = file.readline().strip()
            if not dish_name:
                break
            ingredient_count: int = int(file.readline().strip())
            ingredients: list = []

            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict[str, dict]:
    shop_list: dict = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                if name not in shop_list:
                    shop_list[name] = {'measure': ingredient['measure'], 'quantity': 0}
                shop_list[name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


def merge_files(file_list: str, output_file: str) -> None:
    file_info: list = []

    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_info.append((file_name, len(lines), lines))

    file_info.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, lines in file_info:
            out_file.write(f"{file_name}\n{line_count}\n")
            out_file.writelines(lines)


cook_book = read_cook_book('recipes.txt')
pprint(cook_book)

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(shop_list)

file_list = ['2.txt', '3.txt', '21.txt']
merge_files(file_list, 'merged.txt')
