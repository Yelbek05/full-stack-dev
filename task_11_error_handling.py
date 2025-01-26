class NegativeNumError(Exception):
    pass

def check_positive(value, value_name):
    if value <= 0:
        raise NegativeNumError(f"Ошибка! {value_name} Количество продуктов не может быть отрицательным.")
    
def calculation_product():  
    while True:
        try:
            product = int(input("Кол-во продуктов: "))
            check_positive(product, "Количество продуктов")
            return product
        except ValueError:
            print("Ошибка! Введите числовое значение.")
        except NegativeNumError as e:
            print(e)
        
def calculation_price():
    while True:
        try:
            price = float(input("Введите цену одного продукта:"))
            check_positive(price, "Цена одного продукта")
            return price
        except ValueError:
            print("Ошибка! Введите числовое значение.")
        except NegativeNumError as e:
            print(e)

def main():
    product_amount = calculation_product() 
    price = calculation_price()

    total = product_amount * price
    print(f"Total: {total:.2f}")

if __name__ == '__main__':
    main()