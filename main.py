import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#partie1
df = pd.read_csv("C:\\Users\\AdMin\\Downloads\\employees2 (1).csv")

print("Aperçu du DataFrame :")
print(df.head())

print("Types de données :")
print(df.dtypes)

print("Valeurs manquantes par colonne :")
print(df.isnull().sum())

#partie2

median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

df["Salary"] = df.groupby("Department")["Salary"].transform(lambda x: x.fillna(x.mean()))

df["Age"] = df["Age"].astype(int)
df["Years_Experience"] = df["Years_Experience"].astype(float)
df["Salary"] = df["Salary"].astype(float)

df["Remote"] = df["Remote"].replace({"Yes": "Oui", "No": "Non"})

conditions = [
    df["Years_Experience"] < 3,
    df["Years_Experience"].between(3, 7),
    df["Years_Experience"].between(8, 15),
    df["Years_Experience"] > 15
]
labels = ["Junior", "Intermédiaire", "Senior", "Expert"]
df["Ancienneté_Catégorie"] = np.select(conditions, labels, default="Non défini")
print(df)



#partie3
salaire_moyen = df["Salary"].mean()
print("Salaire moyen global :", salaire_moyen)

employe_max_salaire = df.loc[df["Salary"].idxmax()]
print("Employé avec le salaire max :")
print(employe_max_salaire)

print("Salaire moyen par département :")
print(df.groupby("Department")["Salary"].mean())

print("Moyenne et médiane par ancienneté :")
print(df.groupby("Ancienneté_Catégorie")["Salary"].agg(["mean", "median"]))

print("Employés en télétravail par département :")
print(df[df["Remote"] == "Oui"].groupby("Department").size())

#challenge4

pivot_salaire = pd.pivot_table(df, values="Salary", index="Department", columns="Remote", aggfunc="mean")
print("Salaire moyen par département et télétravail :")
print(pivot_salaire)

df["Groupe_Age"] = pd.cut(df["Age"], bins=[20, 30, 40, 50, 60, 70], labels=["20-30", "31-40", "41-50", "51-60", "61-70"])
pivot_exp = pd.pivot_table(df, values="Years_Experience", index="Groupe_Age", columns="Department", aggfunc="mean")
print("Expérience moyenne par groupe d’âge et département :")
print(pivot_exp)

#challenge5
df["Performance"] = np.where(
    df["Salary"] < 60000, "Bon",
    np.where(df["Salary"] < 80000, "Moyen", "Haut")
)

conditions = [
    (df["Age"] < 35) & (df["Years_Experience"] < 5),
    (df["Age"] < 35) & (df["Years_Experience"] >= 5),
    (df["Age"] >= 35) & (df["Years_Experience"] < 5),
    (df["Age"] >= 35) & (df["Years_Experience"] >= 5)
]
choices = ["Jeune & Nouveau", "Jeune & Expérimenté", "Senior & Nouveau", "Senior & Expérimenté"]
df["Profil"] = np.select(conditions, choices, default="Non défini")


df["Écart_Salaire_Département"] = df["Salary"] - df.groupby("Department")["Salary"].transform("mean")

#BONUUUS

plt.figure(figsize=(8,5))
sns.histplot(df["Salary"], kde=True, color="skyblue")
plt.title("Distribution des salaires")
plt.xlabel("Salaire")
plt.ylabel("Fréquence")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Department", y="Salary", estimator=np.mean)
plt.title("Salaire moyen par département")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x="Ancienneté_Catégorie", y="Salary")
plt.title("Boxplot des salaires par ancienneté")
plt.show()
