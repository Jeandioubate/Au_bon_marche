# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-

import classes

#  Init variables
# Cash register variable = Primeur()
cash_register = classes.Primeur()
stock: classes.Product
menu_choice: int = -1

# Menu
while menu_choice != 0:
    print("Welcome to Au bon marché !")
    print("Menu")
    print("1 - New sell")
    print("2 - Display current stock")
    print("3 - Display balance sheet")
    print("0 - Quit")
    menu_choice = int(input("What do you want to do ?"))
    match menu_choice:
        case 0:
            break
        case 1:
            # New sell
            finish = False
            while not finish:
                client_name = str(input("Please enter the client's lastname : \n"))
                client_firstname = str(input("Please enter the client's firstname : \n"))
                new_sell = classes.Client(client_name, client_firstname)
                cash_register.show_stock()
                product_name = str(input("What product do you want to purchase ? (type product's name\n"))
                product_quantity = float(input("What quantity do you want to buy ? (type a float number)\n"))
                new_sell.add_purchase(product_name, product_quantity)
                finish_choice = int(input("Continue purchase ?\n 0 - No\n 1 - Yes\n"))
                if finish_choice == 0:
                    finish = True
                else:
                    finish = False
        case 2:
            # Display stock
            cash_register.show_stock()
        case 3:
            # TODO : use new function to display balance
            cash_register.show_stock()

print("Goodbye !")
