def save_to_file(name, age, color):
    file_path = "/home/abstract/full-stack-dev/Devcore102/task_3_io/user_info.txt"
    try:
        with open(file_path, "w") as file: 
            file.write(f"Name: {name}, Age: {age}, Favorite color: {color}")
        print("The information is successfully added")
    #In case when the written text is not saved correctly
    except ValueError as e:
        print(f"An error occured while writing to the {e}")

def main():
    name = input("What's your name? ")
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("Enter the valid number, please!")
    color = input("What's your favorite color? ")

    while True:
        print("What do you want?")
        print("1. Show to right up to the interface")
        print("2. Save it to the file, then show in there")
    
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Name: {name}, Age: {age}, Favorite color: {color}")
            break
        elif choice == '2':
            save_to_file(name, age, color)
            break
        else:
            print("Please, enter the valid number: ")

if __name__ == '__main__':
    main()