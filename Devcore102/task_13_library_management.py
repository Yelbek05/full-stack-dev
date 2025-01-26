import json

class Book:
    def __init__(self, id, title, isbn, author):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.id}. '{self.title}' — {self.author}, isbn: {self.isbn}"
    
class Library:
    def __init__(self):
        self.books = {}

    def display_available_books(self):
        print("Доступные книги в библиотеке:")
        for id, book in self.books.items():
            if book.is_available:
                print(book)

    def get_books(self):
        return [
            (1, "1984", "Джордж Оруэлл", "978-0-452-28423-4"),
            (2, "Мастер и Маргарита", "Михаил Булгаков", "978-5-699-49256-5"),
            (3, "Қыз Жібек", "Жүсіпбек Аймауытов",  "978-601-03-0000-3"),
            (4, "Абай жолы", "Мұхтар Әуезов", "978-601-03-0000-3"),
            (5, "Преступление и наказание", "Федор Достоевский", "978-5-699-49256-5")
        ]
    
    def add_book(self):
        try:
            id = int(input("Введите id книги: "))
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            isbn = input("Введите isbn книги: ")
            book = Book(id, title, isbn, author)
            self.books[id] = book
            print(f"Книга '{title}' добавлена в библиотеку.")
            self.display_available_books()
        except ValueError:
            print("Некорректный ввод, введите число.")

    def search_book_by_title(self):
        title = input("Введите название книги: ")
        for book in self.books.values():
            if title.lower() in book.title.lower():
                print(book)

    def list_available_books(self):
        print("Доступные книги в библиотеке:")
        for book in self.books.values():
            if book.is_available:
                print(f"{book.id}. '{book.title}' — {book.author}, isbn: {book.isbn}")
    
    def borrow_book(self):
        title = input("Введите название книги: ").lower()
        for book in self.books.values():
            if title in book.title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"Книга '{book.title}' выдана вам.")
                else:
                    print(f"Книга '{book.title}' уже выдана, вы можете забрать когда она будет доступна.")
    def return_book(self):
        title = input("введите название книги: ").lower()
        for book in self.books.values():
            if title in book.title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"Книга '{book.title}' возвращена в библиотеку.")
                else:
                    print(f"Книга '{book.title}' уже в библиотеке.")

def main():
    library = Library()

    books = library.get_books()
    for book in books:
        id, title, author, isbn = book
        library.books[id] = Book(id, title, author, isbn)
    library.display_available_books()

    user = input("Введите ваше имя: ")

    while True:
        print("\nВыберите действие: ")
        library_actions = {
            1: "добавление книги в библиотеку.",
            2: "поиск книги по названию (частичное совпадение).",
            3: "вывод списка всех доступных книг.",
            4: "выдача книги пользователю, если она доступна.",
            5: "возврат книги в библиотеку.",
            6: "выход из программы."
            }
        
        for number, action in library_actions.items():
            print(f"{number}. {action}")

        choice = input("Ваш выбор: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.search_book_by_title()

        elif choice == "3":
            library.display_available_books()

        elif choice == "4":
            library.borrow_book()
        
        elif choice == "5":
            library.return_book()

        elif choice == "6":
            break

if __name__ == "__main__":
    main()