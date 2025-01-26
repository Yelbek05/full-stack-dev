user_info = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice67@gmail.com"},
    {"id": 2, "name": "Jeksen", "age": 30, "email": "jeksen54@gmail.com"},
    {"id": 3, "name":"Yelbek", "age": 19, "email": "elbekmoldabay@gmail.com"}
]

def Print_user():
    for user in user_info:
        print(f"ID: {user['id']}, Name: {user['name']} Age: {user['age']}, email: {user['email']}")
    print()

class User_Info_dict:
    def __init__(self):
        #Global) global user_info, but changed the Global to Local
        self.user_info = user_info
#Adding new Users to user_info
    def add_user(self):
        print("Add new user")
        user_id = len(user_info) + 1
        user_name = input("Name:")
        user_age = int(input("Age: "))
        user_email = input("@mail:") 

        for user in user_info:
            if user["name"] == user_name:
                print("User already exists, please add another user")
                return 
        
        user_info.append({
            "id": user_id,
            "name": user_name,
            "age": user_age,
            "email": user_email
            })
        
        print("Updated Dict of Users")
        for user in user_info:
            print(f"ID: {user['id']}, Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")
        print()
#Deleting new users from user_info
    def delete_user(self):
        print("Current Users are: ")
        for user in self.user_info:
            print(f"ID: {user['id']}, Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")
        print()

        user_id = int(input("Enter the User ID to delete: "))
        for user in self.user_info:
            if user["id"] == user_id:
                user_info.remove(user)
                print("user is successfully removed")
                return 
        
        print("No user found with that ID")
def main_thing():
    users = User_Info_dict()
    while True:
        print("Choose the action to perform")
        print("1. Print exisiting users")
        print("2. Add a new user")
        print("3. Delete an existing user")
        print("4. Exit")

        choice = input("The number of action: ")
        if choice == '1':
            print(Print_user())
        elif choice == '2':
            print(users.add_user())
        elif choice == '3':
            print(users.delete_user())
        elif choice == '4':
            print("Program has ended, bye bye!")
            break
        else:
            print("Your entered number is invalid, please enter the valid number")
if __name__ == "__main__":
    main_thing()
