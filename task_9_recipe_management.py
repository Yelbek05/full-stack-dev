recipes = {
    "Pasta": ["Томаты", "Сыр", "Спагетти"],
    "Salad": ["Огурцы", "Томаты", "Листья салата"]
}
print(f"Доступные рецепты:")
for recipe, ingredient in recipes.items():
    ingridients_str = ", ".join(ingredient)
    print(f"- {recipe}: {ingridients_str}")

ingredient_prices = {
    "Томаты": ["500 тенге"],
    "Сыр": ["2000 тенге"],
    "Спагетти": ["1500 тенге"],
    "Огурцы": ["300 тенге"],
    "Листья салата": ["700 тенге"]
} 
print()

print("Доступные ингредиенты:")
for key, value in ingredient_prices.items():
    value_str = ", ".join(value)
    print(f"- {key}: {value_str}")

#Adding a new recipe with prices
def Add_new_recipe(recipes, ingridient_prices):
    #Recipe adding
    num_entries = int(input("Сколько блюд вы хотите Внести?(1? 2?): "))
    for i in range(num_entries):
        key = input("Введите название нового блюда: ")
        values = input("Введите ингредиенты через запятую: ").split(",")
        recipes[key] = values
    #Adding prices
        for ingridient in values:
            ingridient_price = float(input(f"Введите стоимость нового ингредиента {ingridient}: "))
            ingridient_prices[ingridient] = ingridient_price
    print("Рецепт добавлен!")

def Recipe_calculation(recipes,ingridient_prices):
    meal_name = input("Введите название рецепта: ")
    
    if meal_name in recipes:
        print(f"Ингредиенты для {meal_name}:")
        for ingredient in recipes[meal_name]:
            if ingredient in ingredient_prices:
                print(f"- {ingredient}: {ingredient_prices[ingredient]} тенге")
    
    else:
        print("Нет такого рецепта")
def main():
    print("Выберите действие: ")
    print("1. Добавить новый рецепт")
    print("2. Рассчитать стоимость рецепта")

    choice = input("Ваш выбор: ")

    if choice == '1':
        Add_new_recipe(recipes, ingredient_prices)
    if choice == '2':
        Recipe_calculation(recipes, ingredient_prices)
if __name__ == '__main__':
    main()