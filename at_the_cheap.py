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
    print("Bienvenue Au bon marché !")
    print("Menu")
    print("1 - Nouvelle vente")
    print("2 - Afficher le stock actuel")
    print("3 - Afficher le rapport quotidien")
    print("0 - Quitter")
    try:
        menu_choice = int(input("Que voulez-vous faire ?\n"))
    except ValueError:
        print("Erreur : Choisissez une option entre 0 et 3.")
        menu_choice = -1
    match menu_choice:
        case 0:
            break
        case 1:
            # New sell
            client_name = str(input("S'il vous plait, veuillez saisir le nom du client : \n"))
            client_firstname = str(input("S'il vous plait, veuillez saisir le prénom du client : \n"))
            new_sell = classes.Client(client_name, client_firstname)
            finish = False
            while not finish:
                cash_register.show_stock()
                product_name = ""
                while product_name not in cash_register.products:
                    product_name = str(input("Quel produit souhaitez-vous acheter ? (Tapez le nom du produit\n"))
                product_quantity = -1
                while product_quantity == -1:
                    try:
                        product_quantity = float(input("Quelle quantité souhaitez-vous acheter ? (Saisissez un nombre décimal)\n"))
                    except ValueError:
                        print("Erreur : La valeur doit être un nombre positif.")
                new_sell.add_purchase(product_name, product_quantity)
                finish_choice = -1
                while finish_choice not in (0,1):
                    try:
                        finish_choice = int(input("Poursuivre l'achat ?\n 0 - Non\n 1 - Oui\n"))
                    except ValueError:
                        print("Erreur : La valeur doit être comprise entre 0 et 1")
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
            print("Erreur : Vous devez saisir un nombre compris entre 0 et 3.")
            menu_choice = -1

print("A bientôt !")
