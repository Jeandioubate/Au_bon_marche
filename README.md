# Au bon marché
## Caisse en ligne de commande

### Sommaire
[But du programme](#but-du-programme)

[Manuel d'utilisation](#manuel-dutilisation)

[Classes et méthodes](#classes-et-méthodes)

[Notes](#notes)

### But du programme

« Au bon marché » est un primeur vendant des fruits et légumes de saison, à la pièce ou au kilo. Le tableau suivant recense le stock et les différents prix début janvier 2025. Le programme a pour but de permettre aux clients de la journée de faire leurs achats en choisissant les fruits et légumes souhaités (et leur quantité).

### Manuel d'utilisation

Au lancement du programme, un menu permet de traiter l’arrivée d’un client ou d’éditer le bilan de la journée. À son arrivée, un client indique son nom et son prénom et un menu lui permet de remplir au fur et à mesure son panier. Une fois qu’il a indiqué que ses achats sont terminés, un ticket de caisse lui est affiché, récapitulant ses achats et totalisant la somme à payer. Le stock de chaque fruit et légume est naturellement tenu à jour après chaque achat. Le bilan de la journée permet quant à lui d’afficher la liste des clients, le total de leur achat, ainsi que le stock restant de chaque fruit et légume.

### Classes et méthodes
- Produit :
	- Attributs :
		- Nom
		- Type_pdt
		- Prix unitaire
		- Type_prix (kg/unité)
		- Stock initial
		- Stock courant
	- Méthodes :
		- Vendre(qte)
		- Afficher_produit
- Client :
	- Attributs :
		- Nom
		- Prénom
		- Panier {nom_produit : qté}
	- Méthodes :
		- Ajouter_achat(produit, qté)
		- Total()
		- Afficher ticket()
- Primeur :
	- Attributs :
		- Produits []
		- Client []
	- Méthodes :
		- Ajouter_produit()
		- Nouveau_client (nom, prénom)
		- Afficher bilan()
		- Afficher stock()

### Notes

- Suggestions d'ajout :
	- Séparer calculs et affichage
		- Primeur : méthode Calculer_bilan
		- Client : total_produit
