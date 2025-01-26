def main():
    while True:
        #a - amount
        try:
            a = int(input("Enter the amount of product you bought: "))
            if a < 0:
                print("The amount cannot be negative")
                continue
        except ValueError:
            print("Write the (valid) number please")  

        #List of product_prices
        prices = []
        for i in range(a):
            product_pricea = (input(f"Enter the {i+1} product's price, or stop: ")).lower()
            if product_pricea == 'stop':
                break
            try:
                product_price = int(product_pricea)
                prices.append(product_price)
            except ValueError:
                print("Please enter the correct number")
        #10% discount 
        ten_discount = list(map(lambda x: x * 0.9 if x > 100 else x, prices))
        print(f"Recounting prices with discount {ten_discount}")

        #filter 
        filtering = list(filter(lambda x: x > 100, prices))
        print(f"Products' prices which are encountered with a 10% discount {filtering}")

        #Total price
        total_price = 0
        for price in ten_discount:
            total_price += price
        print(total_price)
        break
if __name__ == '__main__':
    main()