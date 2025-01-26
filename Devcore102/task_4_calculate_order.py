#if the price is more than 1000 the total price is considered with 5% and 10%
def loyal_customer_calculation(total_order_price, loyalty_program, add_discount):
    if total_order_price > 1000:
        return total_order_price - (total_order_price * add_discount + total_order_price * loyalty_program)
    else:
        return total_order_price - total_order_price * loyalty_program

#if the price is more than 1000 the 5% is considered
#if the price is less than 1000 NO PERCENT IS CONSIDERED
def more_1000(total_order_price, add_discount):
    if total_order_price > 1000:
        return total_order_price - add_discount * total_order_price
    else:
        return total_order_price
loyalty_program = 0.1 #10%
add_discount = 0.05 #0.05% if the price more than 1000

total_order_price = float(input('Enter the total price of the order: ')) 

loyal_customer = input("Are you a loyal customer? (Yes / No): ").lower()

if loyal_customer == 'yes':
    final_price = loyal_customer_calculation(total_order_price, loyalty_program, add_discount)
    print(f"Final price for participating in the loyalty program is {final_price}")
elif loyal_customer == 'no':
    final_price = more_1000(total_order_price, add_discount)
    print(f"Final price with 5%: {final_price}")
