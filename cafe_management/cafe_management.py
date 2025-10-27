menu = {
    "Pizza": 50,
    "Pasta": 100,
    "burger": 200,
    "Shawarma": 300,
    "Platter": 250,
    "Nahari": 200,
    "Krachi": 150,
    "Baryani": 120,
    "Pay": 700,
    "Plao": 130,
    "Chapli Kabab": 100,
    "Haleem": 180,
    "Chane": 170,
    "Beef Botti": 150,
    "Mutton": 700,
    "Mutton botti": 250,
    "Chiken leg sticks": 230,
    "Butter Chiken": 500,
    "Samosa": 50,
    "Golab Jaman": 50,
    "Lassi": 150,
    "Custurd": 200,
    "salad": 100,
    "Coffie": 320,
    "Chai": 100
}

print("WELCOME TO OUR RESTAURANT ☺️")

print("Pizza: RS 50\nPasta: RS 100\nburger: RS200\nShawarma: RS 300\nPlatter: RS 250\nNahari: RS 200\nKrachi: RS 150\nBaryani: RS 120\nPay: RS 700\nPlao: RS 130\nChapli Kabab: RS 100\nHaleem: RS 180\nChane: RS 170\nBeef Botti: RS 150\nMutton: RS 700\nMutton botti: RS 250\nChiken leg sticks: RS 230\nButter Chiken: RS 500\nSamosa: RS 50\nGolab Jaman: RS 50\nLassi: RS 150\nCusturd: RS 200\nsalad: RS 100\nCoffie: RS 320\nChai: RS 100")

order_total = 0

item_1 = input("Enter the name of item you want to order = ").strip().title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to you order")

else:
    print(f"Your item {item_1} is not available on our Restaurant")

another_item = input("Do you want an other Item? (yes/no)").strip().lower()

if another_item == "yes":
    item_2 = input("Enter your second itme = ").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has added in your order")

    else:
        print(f"Your item {item_2} is not available on our restaurant")

print(f"Your total amount of item is to pay {order_total}")