# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-
from typing import Any


class Client:
    """
    Classe représentant un client
    - name : nom du client
    - firstname : prénom du client
    - basket : dictionnaire de produits dont chaque clé est le nom du produit et la valeur la quantité achetée
    """
    name: str = ""
    firstname: str = ""
    basket: dict[Any, Any] = {}

    def __init__(self, name: str, firstname: str) -> None:
        """

        :param name:
        :param firstname:
        """
        self.name = name
        self.firstname = firstname

    def add_purchase(self, product: str, quantity: int) -> None:
        """
        Usage : add purchase in basket
        :param product: product name
        :param quantity: product quantity
        :return:
        """
        if self.basket[product] == 0:
            self.basket[product] = quantity
        else:
            self.basket[product] += quantity

    def total_purchase(self, products: dict[Any, Any]) -> float:
        """
        Usage : calculate the amount of the purchase's total
        :param products: list of products
        :return:
        """
        total = 0
        for product_purchase in self.basket:
            product_price = self.calculate_product_purchase(products[product_purchase["name"]])
            total += product_price
        return total

    def calculate_product_purchase(self, product: object) -> float:
        """
        Usage : calculate the price of the product with the quantity
        :param product:
        :return:
        """
        return self.basket[product].quantity * product.price