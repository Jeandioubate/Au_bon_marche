# Au bon marché
## Caisse en ligne de commande

### Sommaire
[But du programme](#but-du-programme)

[Manuel d'utilisation](#manuel-dutilisation)

[Classes et méthodes](#classes-et-méthodes)

[Notes](#notes)

### Principes du programme

« Au bon marché » est un primeur vendant des fruits et légumes de saison, à la pièce ou au kilo. Le tableau suivant recense le stock et les différents prix début janvier 2025. Le programme a pour but de permettre aux clients de la journée de faire leurs achats en choisissant les fruits et légumes souhaités (et leur quantité).


Article			|Quantité	|Prix unitaire
-------------------------------------------------------
Clémentine		|6 kg		|2,90 € / kg
Carotte			|7 kg		|1,30 € / kg
Datte			|4 kg		|7,00 € / kg
Choux de Bruxelles	|4 kg		|4,00 € / kg
Grenade			|3 kg		|3,50 € / kg
Chou vert		|12 pièces	|2,50 € / pièce
Kaki			|3 kg		|4,50 € / kg
Courge butternut	|6 pièces	|2,50 € / pièce
Kiwi			|5 kg		|3,50 € / kg
Endive			|5 kg		|2,50 € / kg
Mandarine		|6 kg		|2,80 € / kg
Épinard			|4 kg		|2,60 € / kg
Orange			|8 kg		|1,50 € / kg
Poireau			|5 kg		|1,20 € / kg
Pamplemousse		|8 pièces	|2,00 € / pièce
Potiron			|6 pièces	|2,50 € / pièce
Poire			|5 kg		|2,50 € / kg
Radis noir		|10 pièces	|5,00 € / pièce
Pomme			|8 kg		|1,50 € / kg
Salsifis		|3 kg		|2,50 € / kg
-------------------------------------------------------

Au lancement du programme, un menu permet de traiter l’arrivée d’un client ou d’éditer le bilan de la journée. À son arrivée, un client indique son nom et son prénom et un menu lui permet de remplir au fur et à mesure son panier. Une fois qu’il a indiqué que ses achats sont terminés, un ticket de caisse lui est affiché, récapitulant ses achats et totalisant la somme à payer. Le stock de chaque fruit et légume est naturellement tenu à jour après chaque achat. Le bilan de la journée permet quant à lui d’afficher la liste des clients, le total de leur achat, ainsi que le stock restant de chaque fruit et légume.

### Manuel d'utilisation



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
