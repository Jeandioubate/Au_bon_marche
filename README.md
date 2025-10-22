# Il s'agit d'un projet en binôme

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
		- Nouveau_client(nom, prénom)
		- Afficher bilan()
		- Afficher stock()

Suggestions d'ajout :
Séparer calculs et affichage
Primeur : méthode Calculer_bilan
Client : total_produit
