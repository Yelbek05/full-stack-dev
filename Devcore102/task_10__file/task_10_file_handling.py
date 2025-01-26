import json
import os
recipes = {
    "Pasta": ["Томаты", "Сыр", "Спагетти"],
    "Salad": ["Огурцы", "Томаты", "Листья салата"]
}

file_path = "/home/abstract/full-stack-dev/Devcore102/task_10__file/task_10.txt"

def download_file(file_path):
    if not os.path.exists(file_path):
        print("Файл {file_path} unfounded")
        return
    with open(file_path, "r") as file:
        try:
            recipes = json.load(file)    
            print("Рецепты загружены из файла task_10.txt.")
        except json.JSONDecodeError:
            print("Файл пуст или содержит не корректный JSON")
def write_file(recipes, file_path):
    with open(file_path, "w") as file:
        json.dump(recipes, file, ensure_ascii=False, indent=5) #Save it as JSON
    print("Рецепты сохранены в файл task_10.txt")

def show_downloaded_file(file_path):
    with open(file_path, "r") as file:
        recipes = json.load(file)
        print("Показать рецепты: ")
        for meal, ingredient in recipes.items():
            print(f"- {meal}: {', '.join(ingredient)}")
def main():
    print("Выберите один из этих")
    print("1. Сохранить рецепты в файл")
    print("2. Загрузить рецепты из файла")
    print("3. Показать загруженные рецепты")
    
    choice = input("Вводите опцию который вы выбрали: ")

    if choice == '1':
        write_file(recipes, file_path)
    elif choice == '2':
        download_file(file_path)
    elif choice == '3':
        show_downloaded_file(file_path)
if __name__ == '__main__':
    main()