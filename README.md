# Au bon marché
## Caisse en ligne de commande

### Sommaire
[But du programme](#but-du-programme)

[Manuel d'utilisation](#manuel-dutilisation)

[Classes et méthodes](#classes-et-méthodes)

[Notes](#notes)

### Principes du programme

« Au bon marché » est un primeur vendant des fruits et légumes de saison, à la pièce ou au kilo. Le tableau suivant recense le stock et les différents prix début janvier 2025. Le programme a pour but de permettre aux clients de la journée de faire leurs achats en choisissant les fruits et légumes souhaités (et leur quantité).

<img width="866" height="395" alt="{2EE8C1E3-8D97-4B98-AD73-A367BDF11E60}" src="https://github.com/user-attachments/assets/cba6cba3-9e51-472d-8ac0-00928621b09f" />
Au lancement du programme, un menu permet de traiter l’arrivée d’un client ou d’éditer le bilan de la journée. À son arrivée, un client indique son nom et son prénom et un menu lui permet de remplir au fur et à mesure son panier. Une fois qu’il a indiqué que ses achats sont terminés, un ticket de caisse lui est affiché, récapitulant ses achats et totalisant la somme à payer. Le stock de chaque fruit et légume est naturellement tenu à jour après chaque achat. Le bilan de la journée permet quant à lui d’afficher la liste des clients, le total de leur achat, ainsi que le stock restant de chaque fruit et légume.

### Manuel d'utilisation

- Pour démarrer le programme, lancer le fichier at_the_cheap.py avec Python
- Un menu s'affiche avec plusieurs options :
- Nouvelle vente :
	- Permet de vendre un article
		- Il faut entrer les noms et prénoms du client
		- Le stock s'affiche alors et l'utilisateur doit entrer le nom de l'article (en respectant la casse) puis entrer la quantité qu'il veut acheter
		- Une fois les achats terminés, l'utilisateur doit indiquer qu'il a fini
		- Le ticket de la vente s'affiche alors puis le programme retourne au menu principal
- Afficher le stock courant
	- Affiche le stock courant du magasin
- Afficher le bilan de la journée :
	- Affiche le bilan de la journée, avec les noms des clients et le total de leurs achats, ainsi que le stock courant et le total des ventes de la journée
- Quitter :
	- Permet de quitter l'application

Chaque option est précédée d'un nombre qu'il faut entrer pour accéder à la fonctionnalité.


### Classes et méthodes
- Produit :
	- Attributs :
		- name : Nom du produit
		- product_type : type du produit (fruit ou légume)
		- price : prix au kg ou à la pièce
		- unit : indique si le prix est au kg ou à la pièce
  		- quantity : quantité en stock
	- Méthodes :
		- sell
- Client :
	- Attributs :
		- name
		- firstname
		- basket
	- Méthodes :
		- add_purchase
		- total_purchase
  		- calculate_product_purchase
- Primeur :
	- Attributs :
		- products
		- clients
	- Méthodes :
		- Ajouter_produit()
		- Nouveau_client (nom, prénom)
		- Afficher bilan()
		- Afficher stock()
