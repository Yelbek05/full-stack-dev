recipes = {
    "Борщ": 3000,
    "Плов": 2500,
    "Салат": 1500,
    "Бифштекс": 5000
}
#available recipes for cooking
def recipes_available_cooking(recipes, budget):
    available_recipes = []
    for meal, price in recipes.items():
        if price <= budget:
            available_recipes.append(meal)
    print(f"Рецепты, которые вы можете приготовить: {available_recipes}")

def bubble_sort(recipes):  
    items = list(recipes.items())
    for i in range(0, len(items)):
        for j in range(len(items) - i - 1):
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    sorted_recipe = [k[0] for k in items]
    print(f"Сортировка рецептов по стоимости: {sorted_recipe}")

def main(recipes):
    print("Доступные рецепты:")
    id = 0
    for key, value in recipes.items():
        id+=1
        print(f"{id}. {key} — {value} тг.")
    print()

    while True:
        user_input = input("Введите свой бюджет: ")  
        if user_input == 'стоп':
            print("Ввод постановлено")
            break
        else:
            budget = int(user_input)
            if budget < 1500:
                print("Ваш бюджет слишком мало, убедитесь чтобы ваш бюджет был не меньше 1500 тг")
                continue
            bubble_sort(recipes)
            recipes_available_cooking(recipes, budget)

if __name__ == '__main__':
    main(recipes)
    
    
