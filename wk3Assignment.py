#defining the function and calculating discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    return price

# make sure price is a positive figure
while True:
    try:
        price = float(input("Enter the price of the item: "))
        if price >= 0:
            break
        print("Price must be a positive number.")
    except ValueError:
        print("Invalid input. Enter a number.")

# make sure discount is between 0 and 100
while True:
    try:
        discount_percent = float(input("Enter the discount percentage (0-100): "))
        if 0 <= discount_percent <= 100:
            break
        print("Discount must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Enter a number.")

# Calculating final price
final_price = calculate_discount(price, discount_percent)
if final_price == price:
    print(f"No discount applied. Original price: kshs.{price}")
else:
    print(f"Final price after discount: kshs.{final_price}")
