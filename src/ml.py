import pandas as pd
import numpy as np

# chargement des datasets
train = pd.read_csv("results_train.csv")
test = pd.read_csv("results_test.csv")

print("train shape :", train.shape)
print("test shape :", test.shape)

# charger correctement le fichier Excel
df_jee = pd.read_excel(
    "je-e-21.03.01.xlsx",
    sheet_name="Schweiz - Gemeinden",
    header=5
)

# nettoyer nom de colonnes
df_jee.columns = df_jee.columns.str.strip()

print("\nColonnes disponibles dans df_jee :")
for col in df_jee.columns:
    print(col)

# trouver automatiquement la colonne commune
commune_col = None
for col in df_jee.columns:
    if "Number" in col or "commune" in col.lower():
        commune_col = col
        break

if commune_col is None:
    raise Exception("Impossible de trouver la colonne des communes")
print("\nColonne utiliser pour Id :", commune_col)

# preparer le dataset
df_jee[commune_col] = pd.to_numeric(df_jee[commune_col], errors='coerce')
df_jee = df_jee.dropna(subset=[commune_col])
df_jee["Id"] = df_jee[commune_col].astype(int).astype(str)

#MERGE
train["Id"] = train["Gemeinde-Nummer"].astype(str)
test["Id"] = test["Gemeinde-Nummer"].astype(str)

#fusionnons le train avec les données démographiques jointure avec id
train = train.merge(df_jee, on="Id", how="left")
test = test.merge(df_jee, on="Id", how="left")

print("\nshape apres merge :", train.shape)

# y = target
y = train["Ja in Prozent"]


# colonnes interdites (leakage)
#supprimons les colonnes qui révèlent directement le résultat du vote
leakage_cols = [
    "Ja in Prozent",
    "Ja-Stimmen",
    "Nein-Stimmen",
    "eingelegte Stimmzettel",
    "Stimmbeteiligung",
    "leere Stimmzettel",
    "ungültige Stimmzettel",
    "gültige Stimmen"
]

# supprimer uniquement celles présentes
train = train.drop(columns=[col for col in leakage_cols if col in train.columns])

# X = features
X = train.select_dtypes(include=[np.number])

X_test = test.reindex(columns=X.columns, fill_value=0)
print("shape X :", X.shape)
# gerer les NaN
from sklearn.impute import SimpleImputer

imp = SimpleImputer(strategy="mean")
X = imp.fit_transform(X)
X_test = imp.transform(X_test)

print("NaN traites")

# modele PCR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

model = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=10)),
    ("reg", LinearRegression())
])

model.fit(X, y)

print("modele PCR entraine")

# Prediction
pred = model.predict(X_test)

print("Prédictions faites")

# fichier Kaggle
submission = pd.DataFrame({
    "Id": test["Id"],
    "Predicted": pred
})

submission.to_csv("submission.csv", index=False)

print("submission.csv cree")