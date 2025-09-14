Exercice : Analyse approfondie des employés d’une entreprise tech
Partie 1 : Chargement et exploration du dataset
Charger le fichier employees2.csv dans un DataFrame Pandas.
Afficher les premières lignes du DataFrame.
Vérifier les types de données de chaque colonne.
Identifier les valeurs manquantes par colonne.

Partie 2 : Nettoyage des données
5. Remplacer les valeurs manquantes dans la colonne Age par la médiane de cette colonne.
Remplir les valeurs manquantes dans Salaire en utilisant la moyenne par département .
Convertir toutes les colonnes numériques en type approprié (float ou int).
Remplacer les valeurs 'Yes'/'No' dans Remote par 'Oui'/'Non'.
Créer une nouvelle colonne Ancienneté_Catégorie qui classe les années d’expérience en :
Junior : < 3 ans
Intermédiaire : 3–7 ans
Senior : 8–15 ans
Expert : > 15 ans

Partie 3 : Analyses exploratoires et statistiques
10. Calculer le salaire moyen global.
Trouver l’employé(e) avec le salaire le plus élevé.
Calculer le salaire moyen par département.
Calculer la moyenne et la médiane des salaires par groupe d’ancienneté.
Compter combien d’employés travaillent en télétravail (Remote) par département.

Partie 4 : Tableaux croisés dynamiques (pivot tables)
15. Créer un tableau croisé dynamique montrant le salaire moyen par département et par télétravail .
16. Créer un autre tableau croisé dynamique montrant le nombre moyen d’années d’expérience par groupe d’âge et par département .

Partie 5 : Calculs avancés avec NumPy
17. Utiliser np.where() pour créer une colonne Performance :
"Bon" si Salaire < 60000
"Moyen" si 60000 ≤ Salaire < 80000
"Haut" si Salaire ≥ 80000 
18. Utiliser np.select() pour classer les employés selon leur âge et leur ancienneté :
Jeune & Nouveau
Jeune & Expérimenté
Senior & Nouveau
Senior & Expérimenté
19. Calculer la différence entre le salaire de chaque employé et le salaire moyen de son département.

Partie 6 : Visualisation (Bonus)
20. Utiliser Matplotlib ou Seaborn pour :
Afficher la distribution des salaires
Comparer les salaires moyens par département sous forme de barplot
Boxplot des salaires par groupe d’ancienneté
