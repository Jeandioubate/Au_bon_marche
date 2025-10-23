# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-

import classes

#  Init variables
cash_register = classes.Primeur()
stock: classes.Product
menu_choice: int = -1

# Fill stock
# Fruits
stock = classes.Product("Clémentine", 6.0, 2.90, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Datte", 4.0, 7, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Grenade", 3.0, 3.5, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Kaki", 3.0, 2.90, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Kiwi", 5.0, 3.50, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Mandarine", 6.0, 2.80, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Orange", 8.0, 1.50, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Pamplemousse", 8.0, 2, classes.Product.UNIT_PIECE, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Poire", 5.0, 2.50, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)
stock = classes.Product("Pomme", 8.0, 1.50, classes.Product.UNIT_KG, classes.Product.TYPE_FRUIT)
cash_register.add_product(stock)

# Vegetables
stock = classes.Product("Carotte", 7.0, 1.30, classes.Product.UNIT_KG, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Choux de Bruxelles", 4.0, 4.0, classes.Product.UNIT_KG, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Chou vert", 12.0, 2.5, classes.Product.UNIT_PIECE, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Courge butternut", 6.0, 2.50, classes.Product.UNIT_PIECE, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Endive", 5.0, 2.50, classes.Product.UNIT_KG, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Épinard", 4.0, 2.60, classes.Product.UNIT_KG, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Poireau", 5.0, 1.20, classes.Product.UNIT_KG, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Potiron", 6.0, 2.50, classes.Product.UNIT_PIECE, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Radis noir", 10.0, 5.00, classes.Product.UNIT_KG, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)
stock = classes.Product("Salsifis", 3.0, 2.50, classes.Product.UNIT_KG, classes.Product.TYPE_VEGE)
cash_register.add_product(stock)


# Menu
while menu_choice != 0:
    print("Welcome to Au bon marché !")
    print("Menu")
    print("1 - New sell")
    print("2 - Display current stock")
    print("3 - Display daily report")
    print("0 - Quit")
    try:
        menu_choice = int(input("What do you want to do ?\n"))
    except ValueError:
        print("Error : must enter a number between 0 and 3.")
        menu_choice = -1
    match menu_choice:
        case 0:
            break
        case 1:
            # New sell
            client_name = str(input("Please enter the client's lastname : \n"))
            client_firstname = str(input("Please enter the client's firstname : \n"))
            new_sell = classes.Client(client_name, client_firstname)
            finish = False
            while not finish:
                cash_register.show_stock()
                product_name = ""
                while product_name not in cash_register.products:
                    product_name = str(input("What product do you want to purchase ? (type product's name\n"))
                product_quantity = -1
                while product_quantity == -1:
                    try:
                        product_quantity = float(input("What quantity do you want to buy ? (type a float number)\n"))
                    except ValueError:
                        print("Error : value must be a positive number.")
                new_sell.add_purchase(product_name, product_quantity)
                finish_choice = -1
                while finish_choice not in (0,1):
                    try:
                        finish_choice = int(input("Continue purchase ?\n 0 - No\n 1 - Yes\n"))
                    except ValueError:
                        print("Error : value must be a number between 0 and 1")
                        finish_choice = -1
                if finish_choice == 0:
                    finish = True
                else:
                    finish = False
            cash_register.new_client(new_sell)
        case 2:
            # Display stock
            cash_register.show_stock()
        case 3:
            # Display daily report
            cash_register.daily_report()
        case _:
            print("Error : must enter a number between 0 and 3.")
            menu_choice = -1

print("Goodbye !")
