# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Product:
    """Représente un produit du primeur (fruit ou légume)."""
    name: str        # nom du produit
    quantity: float  # quantité disponible (en kg ou à l'unité')
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

@dataclass
class Client:
    """
    Classe représentant un client
    - name : nom du client
    - firstname : prénom du client
    - basket : dictionnaire de produits dont chaque clé est le nom du produit et la valeur la quantité achetée
    """
    name: str
    firstname: str
    basket: dict
    # basket: list

    def __init__(self, name: str, firstname: str) -> None:
        """
        Usage : Create new client
        :param name: Client's name
        :param firstname: Client's firstname
        Note : basket is not initialized
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

    def total_purchase(self, products: list) -> float:
        """
        Usage : calculate the amount of the purchase's total
        :param products: list of products
        :return: total amount of the basket
        """
        total = 0
        for product_purchase in products:
            if product_purchase.name in self.basket:
                product_price = self.calculate_product_purchase(product_purchase.price, self.basket[product_purchase.name])
                total += product_price
        return total

    @staticmethod
    def calculate_product_purchase(price: float, qty: int) -> float:
        """
        Usage : calculate the price of the product with the quantity
        :param price: product's unit price
        :param qty: quantity purchased
        :return:
        """
        return qty * price

class Primeur:
    """Gère le stock du magasin et les clients de la journée."""

    def __init__(self, firstname, name, basket, total_purchase):
        self.products: Dict[str, Product] = {}
        self.clients: List[Client] = []

    def show_stock(self) -> None:
        """Affiche le stock actuel des produits."""
        print("\n STOCK ACTUEL :")
        print("-" * 45)
        for p in self.products.values():
            print(f"{p.name:<20} {p.quantity:.2f} {p.unit:<5} - {p.price:.2f} €/ {p.unit}")
        print("-" * 45)

    def display_ticket(self, client: Client) -> None:
        """Affiche un ticket de caisse pour le client."""
        print("\n Ticket de caisse")
        print(f"Client : {client.firstname} {client.name}")
        print("-" * 40)
        total = 0
        for name, qty in client.basket.values():
            product = self.products[name]
            subtotal = qty * product.price
            print(f"{product.name:<20} {qty:.2f} {product.unit:<5} x {product.price:.2f} € = {qty * product.price:.2f} €")
            total += subtotal
        print("-" * 40)
        print(f"Total à payer : {total:.2f} €")
        print("=" * 40 + "\n")

    def new_client(self, firstname: str, name: str, purchases: Dict[str, float]) -> None:
        """
        Gère l'arrivée d'un nouveau client et ses achats.
        :param firstname: prénom du client
        :param name: nom du client
        :param purchases: dictionnaire {nom_produit: quantité_achetée}
        """
        client = Client(name, firstname)
        print(f"\n🛒 Nouveau client : {client.firstname} {client.name}")

        for product_name, qty in purchases.items():
            if product_name not in self.products:
                print(f"  Produit '{product_name}' non trouvé dans le stock.")
                continue

            product = self.products[product_name]

            if product.sell(qty):
                client.add_purchase(product_name, qty)
                print(f" {qty} {product.unit} de {product.name} ajouté au panier.")
            else:
                print(f" Impossible d'ajouter {qty} {product.unit} de {product.name} (stock insuffisant).")

        # Enregistre le client
        self.clients.append(client)

        # Affiche le ticket de caisse
        self.display_ticket(client)

