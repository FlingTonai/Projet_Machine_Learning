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
- [x] `src/utils.py` créé avec fonctions utilitaires réutilisables
- [x] Notebooks refactorisés pour utiliser `utils.py`

---

### 2. 📊 EDA + Preprocessing (fusionnés)
- [x] Chargement de tous les datasets
- [x] Exploration de la structure (dimensions, colonnes, types)
- [x] Visualisation de la variable cible `Ja in Prozent`
- [x] Exploration + nettoyage du dataset Train
- [x] Exploration + nettoyage du dataset Demo
- [x] Exploration + nettoyage du dataset Revenus
- [x] Exploration + nettoyage du dataset Géo
- [x] Exploration + nettoyage du dataset Réf. précédent
- [x] Merge de tous les datasets
- [x] Analyse des corrélations
- [x] Sauvegarde du dataset final propre

**Décision :** EDA et Preprocessing fusionnés dans un seul notebook pour plus de clarté et de simplicité. Chaque dataset est exploré puis nettoyé directement.

**Fichier :** `notebooks/01_EDA.ipynb`

---

### 3. 🤖 Modèle 1 — Principal Component Regression (PCR)
- [x] Implémentation (PCA + Régression linéaire)
- [x] Choix du nombre de composantes principales (optimisé via cross-validation)
- [x] Cross-validation (5 folds)
- [x] Tuning des hyperparamètres (n_components=69)
- [x] Évaluation (RMSE)

**Motivation :** Modèle assigné par les professeurs. La PCR est utile quand les features sont nombreuses et corrélées entre elles (multicolinéarité). Elle réduit la dimensionnalité via PCA avant d'appliquer une régression linéaire.

**Résultats :**
- RMSE cross-validation : 6.3851
- RMSE train complet : 5.9547
- Meilleur n_components : 69

**Fichier :** `notebooks/02_model_PCR.ipynb`

---

### 4. 🤖 Modèle 2 — Random Forest (au choix)
- [x] Implémentation
- [x] Cross-validation (5 folds)
- [x] Tuning des hyperparamètres v1 (GridSearchCV)
- [x] Tuning des hyperparamètres v2 (correction overfitting)
- [x] Évaluation (RMSE)

**Motivation :** Random Forest est un algorithme d'ensemble non-linéaire qui combine plusieurs arbres de décision. Choisi pour son contraste avec PCR (linéaire vs non-linéaire) et sa capacité à capturer des relations complexes.

**Résultats :**
- RMSE cross-validation : 6.2370
- RMSE train complet : 2.2691 → overfitting identifié
- RMSE Kaggle : 6.4695
- Meilleurs hyperparamètres : n_estimators=500, max_depth=15, max_features=0.3, min_samples_split=5

**Fichier :** `notebooks/03_model_RandomForest.ipynb`

---

### 5. 📤 Soumissions Kaggle
- [x] Soumission PCR (submission_PCR_v1.csv) → Score Kaggle : 6.0280 ✅
- [x] Soumission Random Forest (submission_RF_v1.csv) → Score Kaggle : 6.4695
- [ ] Soumissions itératives pour améliorer le score
- [ ] Meilleur score obtenu : **6.0280 (PCR)** ← soumission finale

**Fichier :** `submissions/`

---

### 6. 📝 Rapport LaTeX
- [ ] Section 1 : Organisation du code
- [ ] Section 2 : EDA
- [ ] Section 3 : Méthodologie
- [ ] Section 4 : Résultats & Discussion

**Fichier :** `report/`

---

### 7. 🎤 Présentation orale
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

## 👤 Répartition du travail

### Membre 1 (toi) — EDA, Modèles & Code
- Mise en place du projet (GitHub, environnement) ✅
- EDA + nettoyage + merge (`01_EDA.ipynb`) ✅
- Implémentation et tuning du modèle Random Forest (`03_model_RandomForest.ipynb`) ✅
- Refactorisation des notebooks avec `src/utils.py` ✅
- Soumissions Kaggle ✅
- Rédaction section **Results & Discussion** du rapport

### Membre 2 — Rapport LaTeX
- Rédaction sections **EDA** et **Code organization** du rapport
- Mise en forme LaTeX du rapport complet
- Relecture et corrections

### Membre 3 — Modèle PCR & Présentation
- Implémentation et tuning du modèle PCR (`02_model_PCR.ipynb`) ✅
- Rédaction section **Methodology** du rapport
- Préparation et coordination des slides (PDF)
- Coordination de la présentation orale

---

## 💡 Notes & Décisions

- **EDA + Preprocessing fusionnés** dans `01_EDA.ipynb` — plus simple et logique pour ce projet
- **Suppression de `02_preprocessing.ipynb`** — devenu inutile
- **Notebooks renommés** : `02_model_PCR.ipynb` et `03_model_XGBoost.ipynb`
- **Leakage identifié dans Train** : colonnes supprimées → `Ja-Stimmen`, `Nein-Stimmen`, `gültige Stimmen`, `eingelegte Stimmzettel`, `leere Stimmzettel`, `ungültige Stimmzettel`, `Stimmbeteiligung`
- **Problèmes résolus dans Demo** : 3 premières lignes = métadonnées supprimées, colonnes `.1` renommées (`Primary/Secondary/Tertiary sector establishments`)
- **Doublons dans Geo** : 180 doublons supprimés (coordonnées identiques)
- **Valeurs manquantes** : gérées avec `SimpleImputer` dans les notebooks des modèles
- **Dataset final** : 1559 lignes × 67 colonnes (train), 669 lignes × 66 colonnes (test)
- **Features les plus corrélées avec Ja in Prozent** :
  - Positive : `65 years or over` (0.40), `Unproductive area in %` (0.36), `Small right-wing parties` (0.31)
  - Négative : `Agricultural area in %` (-0.62), `0-19 years` (-0.45), `Size of households in persons` (-0.44)
- **Refactorisation** : notebooks refactorisés pour utiliser `src/utils.py` → `compute_rmse`, `print_cv_results`, `create_submission`
- **PCR** : meilleur n_components = 69, RMSE CV = 6.3851, RMSE train = 5.9547, RMSE Kaggle = 6.0280
- **Random Forest** : RMSE CV = 6.2370, RMSE train = 2.6276 (overfitting), RMSE Kaggle = 6.4695
- **Conclusion** : PCR généralise mieux malgré un RMSE CV légèrement inférieur à RF → les relations dans les données sont majoritairement linéaires
- **Soumission finale** : PCR (RMSE Kaggle = 6.0280)