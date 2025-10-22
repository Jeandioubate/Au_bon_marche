# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-

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