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
        for i in range(len(self.basket)):
            total += products[self.basket["name"]]["price"] * self.basket[i]["name"]
        for product_purchase in self.basket:
            product_price = products[product_purchase["name"]]["price"] * product_purchase["quantity"]
            total += product_price
        return total