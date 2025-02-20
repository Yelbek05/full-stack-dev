from datetime import datetime 

#Constant numbers
discount_rate = 0.1 
loyalty_rate = 0.07
tax_rate = 0.3


class loyalCustomers:
    def __init__(self, customer_id, customer_name):
        self.id = customer_id
        self.name = customer_name

class Product:
    def __init__(self, product_id, product_name, product_price, product_amount):
        self.id = product_id
        self.name = product_name
        self.price = product_price
        self.amount = product_amount


loyal_customers = [
    loyalCustomers(1, "Maral"),
    loyalCustomers(2, "Samal"),
    loyalCustomers(3, "Aral"),
    loyalCustomers(4, "Karal"),
    loyalCustomers(5, "Yelbek"),
]

products = [
    Product(1, "Bread", 1.50, 20),
    Product(2, "Milk", 2.00, 10),
    Product(3, "Eggs", 3.00, 15),
    Product(4, "Cheese", 5.00, 8),
    Product(5, "Butter", 4.50, 12),
    Product(6, "Chicken", 10.00, 5),
    Product(7, "Rice", 1.20, 25),
    Product(8, "Pasta", 2.50, 18),
    Product(9, "Apples", 1.80, 30),
    Product(10, "Bananas", 1.60, 22),
]

def apply_basic_discount(price, discount_rate):
    return price - price * discount_rate

def is_loyal_customer(customer_name):
    for customer in loyal_customers:
        if customer.name == customer_name:
            return True
        else:
            return False

def apply_loyalty_discount(price, loyalty_rate):
    return price - price * loyalty_rate

def apply_basic_tax(price, tax_rate):
    return price + price * tax_rate

def apply_wildcard_tax(price, tax_rate):
    current_time = datetime.now().minute

    if current_time % 2 == 0:
        return price
    else:
        return price + tax_rate * price

    
def calculate_final_price(price, discount_rate, customer_name, loyalty_rate, tax_rate):
    current_time = datetime.now().minute
    price_after_basic_discount = apply_basic_discount(price, discount_rate)

    if is_loyal_customer(customer_name):
        loyalty_rate == 0.07
        price_after_basic_discount == apply_loyalty_discount(price_after_basic_discount, loyalty_rate)
    
    price_after_tax = apply_basic_tax(price_after_basic_discount, tax_rate)
#Apply an additional 3% tax if the currect minute is odd
    wildcard_tax_rate = 0.03
    final_price = apply_wildcard_tax(price_after_tax, wildcard_tax_rate)

    return round(final_price, 2)

def add_loyal_customer():
    customer_name = input("Customer's name: ")
    customer_id = len(loyal_customers) + 1
    loyal_customers.append(loyalCustomers(customer_id, customer_name))
    print(f"Customer with {customer_name} and ID: {customer_id} added as a loyal_customer: ")
    
    print("Updated Loyal Customers")
    for customer in loyal_customers:
        print(f"ID: {customer.id}, Name: {customer.name}")


def add_new_product():
    product_name = input("Name of the product: ")
    product_price = float(input("Price of the product: "))
    product_amount = int(input("Amount of the product: "))
    product_id = len(products) + 1
    
    new_product = Product(product_id, product_name, product_price, product_amount)
    products.append(new_product)
    print("The new product is successfull added!!!")

    print("Updated list of products")
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Amount: {product.amount}")
def main_thing():
    while True:
        print("Choose the action to perform")
        print("0. Calculate the final price")
        print("1. Add the loyal customer")
        print("2. Add the new product")
        print("3. Get off")

        choice = input("Enter the number for action: ")

        if "0" == choice:
            price = float(input("Enter the price of the product: "))
            customer_name = input("Customer's name: ")
            final_price = calculate_final_price(price, discount_rate, customer_name, loyalty_rate, tax_rate)
            if is_loyal_customer(customer_name):
                print(f"loyalty is calculated for {customer_name}")
            print(f"The final price is: {final_price}")
            print()
        elif "1" == choice:
            add_loyal_customer()
            print()
        elif "2" == choice:
            add_new_product()
        elif "3" == choice:
            print("program has ended")
            break
        else:
            print("Invalid number for action, please enter the valid number")
        

if __name__ == "__main__":
    main_thing()