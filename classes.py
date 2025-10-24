# #!/usr/bin/env python
# #  -*- coding: utf-8 -*-

from dataclasses import dataclass
from itertools import product
from typing import Dict, List


@dataclass
class Product:
    """Représente un produit du primeur (fruit ou légume)."""
    name: str        # nom du produit
    quantity: float  # quantité disponible (en kg ou à l'unité')
    price: float     # prix unitaire
    unit: str        # 'kg' ou 'piece'
    product_type: str
    # Constants
    TYPE_FRUIT = "Fruit"
    TYPE_VEGE = "Vegetable"
    UNIT_KG = "kg"
    UNIT_PIECE = "pièce"

    def __init__(self, name, quantity, price, unit, product_type):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.unit = unit
        self.product_type = product_type

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

    def __init__(self, name: str, firstname: str) -> None:
        """
        Usage : Create new client
        :param name: Client's name
        :param firstname: Client's firstname
        Note : basket is not initialized
        """
        self.name = name
        self.firstname = firstname
        self.basket = {}

    def add_purchase(self, product: str, quantity: float) -> None:
        """
        Usage : add purchase in basket
        :param product: product name
        :param quantity: product quantity
        :return:
        """
        if not product in self.basket.keys():
            self.basket[product] = quantity
        else:
            self.basket[product] += quantity

    def total_purchase(self, products: dict) -> float:
        """
        Usage : calculate the amount of the purchase's total
        :param products: list of products
        :return: total amount of the basket
        """
        total = 0
        for product_purchase in products:
            if product_purchase in self.basket.keys():
                product_price = self.calculate_product_purchase(products[product_purchase].price, self.basket[product_purchase])
                total += product_price
        return total

    @staticmethod
    def calculate_product_purchase(price: float, qty: float) -> float:
        """
        Usage : calculate the price of the product with the quantity
        :param price: product's unit price
        :param qty: quantity purchased
        :return:
        """
        return qty * price

class Primeur:
    """Gère le stock du magasin et les clients de la journée."""

    def __init__(self) -> None:
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
        for product_purchased in self.products:
            if product_purchased in client.basket.keys():
                subtotal = client.basket[product_purchased] * self.products[product_purchased].price
                print(f"{product_purchased:<20} {client.basket[product_purchased]:.2f} {self.products[product_purchased].unit:<5} x {self.products[product_purchased].price:.2f} € = {subtotal:.2f} €")
        total = client.total_purchase(self.products)
        print("-" * 40)
        print(f"Total à payer : {total:.2f} €")
        print("=" * 40 + "\n")

    def new_client(self, client: Client ) -> None:
        """
        Gère l'arrivée d'un nouveau client et ses achats.
        :param client:
        """
        #client = Client(name, firstname) # Je crée un nouvel objet Client.
        print(f"\n Nouveau client : {client.firstname} {client.name}")

        for product_name, qty in client.basket.items(): # Je parcours les achats demandés
            if product_name not in self.products:
                print(f"  Produit '{product_name}' non trouvé dans le stock.") # Je vérifie que chaque produit existe
                continue                                                       # dans le stock

            product = self.products[product_name]

            if product.sell(qty):   # Je vérifie que la quantité demandée est disponible et mets à jour le stock et le

                #client.add_purchase(product_name, qty) # le panier du client.
                print(f" {qty} {product.unit} de {product.name} vendu.")
            else:
                print(f" Stock insuffisant pour {product.name}")

        # J'enregistre le client
        self.clients.append(client)

        # J'affiche le ticket de caisse
        self.display_ticket(client)

    def daily_report(self) -> None:
        """Affiche le bilan de la journée : nombre de clients, chiffre d’affaires et état du stock."""
        print("\n BILAN DE LA JOURNÉE")
        print("=" * 60)

        if not self.clients:
            print("Aucun client n’a été enregistré aujourd’hui.")
            print("=" * 60)
            return

        total_clients = len(self.clients)
        total_revenue = 0.0

        for client in self.clients:
            print(f"\n Client : {client.firstname} {client.name}")
            print("-" * 60)
            client_total = 0.0

            for product_name, qty in client.basket.items():
                if product_name in self.products:
                    product = self.products[product_name]
                    subtotal = product.price * qty
                    client_total += subtotal
                    print(f" - {qty:.2f} {product.unit:<5} de {product.name:<15} {product.price:.2f} €/ {product.unit:<5} -> {subtotal:.2f} €")
                else:
                    print(f" Produit {product_name} non trouvé dans le stock.")

            total_revenue += client_total
            print(f" Total client : {client_total:.2f} €")
            print("-" * 60)

        print("\n RESUME GLOBAL")
        print("-" * 60)
        print(f"Nombre total de clients servis : {total_clients}")
        #print("Liste des clients et du total leurs achats : ")
        #for cli in self.clients:
            #print(f"{cli.name} {cli.firstname} :           {cli.total_purchase(self.products):.2f}€")

        print(f"Chiffre d'affaires total       : {total_revenue:.2f} €")
        print("\n STOCK RESTANT")
        print("-" * 60)
        #print("Stock restant :")
        for p in self.products.values():
            print(f"{p.name:<20} {p.quantity:.2f} {p.unit:<5} restants")
        print("=" * 60)

    def add_product(self, product) -> None:
        """

        :param product:
        :return:
        """
        self.products[product.name] = product

