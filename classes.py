# # !/usr/bin/env python
# # -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Dict, List, Union

@dataclass
class Product:
    """Représente un produit du primeur (fruit ou légume)."""
    name: str
    quantity: float
    price: float
    unit: str


    def sell(self, qty: float) -> bool:
        """
        Vend une certaine quantité du produit.
        Retourne True si la vente est possible (stock suffisant),
        False sinon.
        """
        if qty <= 0:
            print("Quantité invalide")
            return False

        if qty > self.quantity:
            print(f"Stock insuffisant pour {self.name}. Disponible : {self.quantity} {self.unit}.")
            return False

        self.quantity -= qty
        return True

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle lisible du produit.
        """
        return f"{self.name:<20} {self.quantity:.2f} {self.unit:<5} à {self.price:.2f} €/ {self.unit}"


class Client:

    def __init__(self, name: str, firstname: str): # Représente un client et son panier d'achats.
        """

        :param name:
        :param firstname:
        """
        self.name = name
        self.firstname = firstname
        self.basket: Dict[str, Dict[str, Product | float]] = {}


    def add_purchase(self, product: Product, quantity: float):
        """
        Ajoute un produit au panier. Si le produit existe déjà, augmente la quantité.
        Vérifie aussi le stock avec la méthode sell().

        :param product:
        :param quantity:
        :return:
        """
        if product.sell(quantity):  # utilise la méthode de la classe Product
            if product.name not in self.basket:
                self.basket[product.name] = {"product": product, "quantity": quantity}
            else:
                self.basket[product.name]["quantity"] += quantity
            print(f" {quantity} {product.unit} de {product.name} ajouté(e)(s) au panier.")
        else:
            print(f" Impossible d’ajouter {product.name} (stock insuffisant).")


    def total_purchase(self) -> float:
        """Calcule le total des achats du client à partir du panier

        :param self:
        :return:
        """

        total = 0
        for item in self.basket.values():
            product = item["product"]
            quantity = item["quantity"]
            total += quantity * product.price
        return total


    def display_ticket(self) -> None:
        """Affiche un ticket de caisse pour le client."""
        print("\n🧾 Ticket de caisse")
        print(f"Client : {self.firstname} {self.name}")
        print("-" * 40)
        for item in self.basket.values():
            product = item["product"]
            qty = item["quantity"]
            print(f"{product.name:<20} {qty:.2f} {product.unit:<5} x {product.price:.2f} € = {qty * product.price:.2f} €")
        print("-" * 40)
        print(f"Total à payer : {self.total_purchase():.2f} €")
        print("=" * 40 + "\n")