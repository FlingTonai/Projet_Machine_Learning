# 📋 Plan de travail — Projet Machine Learning 2026
**UMONS | Prédiction du vote "Initiative Vache à Cornes" (2018)**

---

## 👥 Équipe
- Membre 1 : ...
- Membre 2 : ...
- Membre 3 : ...
- Groupe Moodle : **Groupe 3**
- Modèle assigné : **Principal Component Regression (PCR)**

---

## ✅ Avancement

### 1. 🛠️ Mise en place du projet
- [x] Création de l'environnement virtuel Python (venv)
- [x] Installation des packages : numpy, pandas, matplotlib, seaborn, scikit-learn, openpyxl, xgboost, jupyter
- [x] Structure de dossiers : data/, notebooks/, src/, report/, submissions/
- [x] Dépôt GitHub créé et lié : https://github.com/FlingTonai/Projet_Machine_Learning
- [x] Datasets téléchargés depuis Kaggle et pushés sur GitHub
- [x] Fichier .gitignore configuré
- [x] requirements.txt généré

---

### 2. 📊 Exploratory Data Analysis (EDA)
- [ ] Chargement de tous les datasets
- [ ] Exploration de la structure (dimensions, colonnes, types)
- [ ] Analyse des valeurs manquantes
- [ ] Visualisation de la variable cible `Ja in Prozent`
- [ ] Analyse des corrélations
- [ ] Détection d'anomalies / outliers
- [ ] Fusion des datasets

**Fichier :** `notebooks/01_EDA.ipynb`

---

### 3. 🔧 Preprocessing
- [ ] Nettoyage des données
- [ ] Gestion des valeurs manquantes
- [ ] Feature engineering
- [ ] Encodage des variables catégorielles
- [ ] Normalisation / standardisation
- [ ] Séparation train/validation

**Fichier :** `notebooks/02_preprocessing.ipynb` ou `src/preprocessing.py`

---

### 4. 🤖 Modèle 1 — Principal Component Regression (PCR)
- [ ] Implémentation (PCA + Régression linéaire)
- [ ] Choix du nombre de composantes principales
- [ ] Cross-validation
- [ ] Tuning des hyperparamètres
- [ ] Évaluation (RMSE)

**Motivation :** Modèle assigné par les professeurs. La PCR est utile quand les features sont nombreuses et corrélées entre elles (multicolinéarité). Elle réduit la dimensionnalité via PCA avant d'appliquer une régression linéaire.

**Fichier :** `notebooks/03_model_PCR.ipynb`

---

### 5. 🤖 Modèle 2 — XGBoost (au choix)
- [ ] Implémentation
- [ ] Cross-validation
- [ ] Tuning des hyperparamètres (n_estimators, max_depth, learning_rate...)
- [ ] Évaluation (RMSE)

**Motivation :** XGBoost est un algorithme de gradient boosting très performant sur les données tabulaires. Il gère bien les valeurs manquantes, les relations non-linéaires et est souvent très compétitif sur ce type de compétition Kaggle.

**Fichier :** `notebooks/04_model_XGBoost.ipynb`

---

### 6. 📤 Soumissions Kaggle
- [ ] Première soumission (baseline)
- [ ] Soumissions itératives
- [ ] Meilleur score obtenu : ...

**Fichier :** `submissions/`

---

### 7. 📝 Rapport LaTeX
- [ ] Section 1 : Organisation du code
- [ ] Section 2 : EDA
- [ ] Section 3 : Méthodologie
- [ ] Section 4 : Résultats & Discussion

**Fichier :** `report/`

---

### 8. 🎤 Présentation orale
- [ ] Slides créées (PDF)
- [ ] Répartition de la parole entre les membres
- [ ] Présentation le 11 ou 12 mai

---

## 📅 Deadlines
| Date | Quoi | Statut |
|------|------|--------|
| 31 mars 2026 | Équipe formée sur Moodle | ✅ |
| 6 mai 2026 | Clôture Kaggle | ⏳ |
| 7 mai 2026 | Rendu rapport + code (.zip) sur Moodle | ⏳ |
| 11-12 mai 2026 | Présentations orales | ⏳ |

---

## 📦 Datasets utilisés
| Fichier | Contenu | Source |
|--------|---------|--------|
| `results_train.xlsx` | Résultats référendum (70% communes) | swissvotes.ch |
| `results_test.csv` | Communes à prédire (30%) | swissvotes.ch |
| `je-e-21.03.01.xlsx` | Données démographiques, géo, économiques | bfs.admin.ch |
| `statistik-dbst-np-kennzahlen-mit-2017-fr.xlsx` | Revenus par commune 2017 | estv.admin.ch |
| `swiss_communes_geodata.csv` | Latitude/longitude des communes | WikiData |
| `622.00-result-...xlsx` | Résultats référendum précédent (souveraineté alimentaire) | swissvotes.ch |

---

## 💡 Notes & Décisions
*(Cette section sera complétée au fur et à mesure)*

- ...