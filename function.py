def validate_number(input_Espresso, input_Cappuccino, input_Latte, input_Mocca):
    if type(input_Espresso) or type(input_Cappuccino) or type(input_Latte) or type(input_Mocca) != int:
        return "Please input an integer"

def display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount):
    Espresso_price = (input_Espresso * 55)
    Cappuccino_price = (input_Cappuccino * 60)
    Latte_price = (input_Latte * 65)
    Mocca_price = (input_Mocca * 70)

    total_price = (Espresso_price + Cappuccino_price + Latte_price + Mocca_price)
    if discount == "y":
        discounts =  (input_Cappuccino + input_Espresso + input_Latte + input_Mocca)*5
        total_price = (total_price - discounts)
        return total_price 
    elif discount == "n":
        return total_price
    else:
        return "Please in put y or n"

