# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-
from typing import Any


class Client:
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

        :param product:
        :param quantity:
        :return:
        """
        if self.basket[product] == 0:
            self.basket[product] = quantity
        else:
            self.basket[product] += quantity

    def total_purchase(self, products: object) -> float:
        """

        :type products: object
        :param products:
        :return:
        """
        total = 0
        for product_purchase in self.basket:
            product_price = self.calculate_product_purchase(products[product_purchase["name"]])
            total += product_price
        return total

    def calculate_product_purchase(self, product: object) -> float:
        """

        :param product:
        :return:
        """
        return self.basket[product["name"]]["quantity"] * product["price"]