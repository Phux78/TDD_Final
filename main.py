from function import display_price

input_Espresso = int(input("Espresso: "))
input_Cappuccino = int(input("Cappuccino: "))
input_Latte = int(input("Latte: "))
input_Mocca = int(input("Mocca: "))
discount = str(input("Discount Y/N: "))

result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)

print(result)