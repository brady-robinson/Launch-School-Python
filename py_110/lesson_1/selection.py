def select_fruit(fresh_food):
    return {key: value for 
            key, value in 
            fresh_food.items() if 
            value == 'Fruit'}

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))