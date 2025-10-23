# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Product:
    """Représente un produit du primeur (fruit ou légume)."""
    name: str        # nom du produit
    quantity: float  # quantité disponible (en kg ou en pièces)
    price: float     # prix unitaire
    unit: str        # 'kg' ou 'piece'

    def sell(self, qty: float) -> bool:
        """
        Vend une certaine quantité du produit.
        Retourne True si la vente est possible (stock suffisant),
        False sinon.
        """
        if qty <= 0:
            print("Quantité invalide.")
            return False

        if qty > self.quantity:
            print(f" Stock insuffisant pour {self.name}. Disponible : {self.quantity} {self.unit}.")
            return False

        self.quantity -= qty
        return True

    def __str__(self) -> str:
        """Retourne une représentation textuelle lisible du produit."""
        return f"{self.name:<20} {self.quantity:.2f} {self.unit:<5} à {self.price:.2f} €/ {self.unit}"


class Client:
    name = ""
    firstname = ""
    basket = {}

    def __init__(self, name, firstname):
        """

        :param name:
        :param firstname:
        """
        self.name = name
        self.firstname = firstname

    def add_purchase(self, product, quantity):
        """

        :param product:
        :param quantity:
        :return:
        """
        if self.basket[product] == 0:
            self.basket[product] = quantity
        else:
            self.basket[product] += quantity

    def total_purchase(self, products):
        """

        :param products:
        :return:
        :return:
        """
        total = 0
        for product_purchase in self.basket:
            product_price = self.calculate_product_purchase(products[product_purchase["name"]])
            total += product_price
        return total

    def calculate_product_purchase(self, product):
        """

        :param product:
        :return:
        """
        return self.basket[product["name"]]["quantity"] * product["price"]