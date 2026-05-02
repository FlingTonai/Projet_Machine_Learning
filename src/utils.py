# =============================================================================
# utils.py
# -----------------------------------------------------------------------------
# Ce fichier contient les fonctions utilitaires réutilisées dans tous
# les notebooks de modélisation du projet.
#
# Fonctions disponibles :
#   - compute_rmse()        : calcule le RMSE entre prédictions et vraies valeurs
#   - print_cv_results()    : affiche les résultats de cross-validation
#   - create_submission()   : crée le fichier de soumission Kaggle
#
#
# Auteurs : Groupe 3 — UMONS 2025-2026
# =============================================================================

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error


def compute_rmse(y_true, y_pred):
    """
    Calcule le RMSE (Root Mean Squared Error) entre les vraies valeurs
    et les prédictions.

    Le RMSE est la métrique d'évaluation officielle de la compétition Kaggle.
    Il est exprimé dans la même unité que la variable cible (% de votes OUI).

    Paramètres :
        y_true (array-like) : vraies valeurs de Ja in Prozent.
        y_pred (array-like) : valeurs prédites par le modèle.

    Retourne :
        rmse (float) : valeur du RMSE.
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


def print_cv_results(rmse_scores, model_name="Modèle"):
    """
    Affiche les résultats de cross-validation de manière lisible.

    Affiche le RMSE par fold, le RMSE moyen et l'écart-type.
    L'écart-type permet d'évaluer la stabilité du modèle.

    Paramètres :
        rmse_scores (array) : tableau des RMSE par fold (valeurs positives).
        model_name (str)    : nom du modèle à afficher.
    """
    print(f"=== {model_name} — Cross-Validation (5 folds) ===")
    print(f"RMSE par fold : {rmse_scores.round(4)}")
    print(f"RMSE moyen    : {rmse_scores.mean():.4f}")
    print(f"RMSE std      : {rmse_scores.std():.4f}")


def create_submission(commune_ids, y_pred, filename="../submissions/submission.csv"):
    """
    Crée le fichier de soumission au format attendu par Kaggle.

    Le fichier CSV contient deux colonnes :
        - Id        : identifiant de la commune
        - Predicted : prédiction du % de votes OUI

    Paramètres :
        commune_ids (array-like) : identifiants des communes du test.
        y_pred (array-like)      : prédictions du modèle.
        filename (str)           : chemin du fichier de soumission à créer.

    Retourne :
        submission (DataFrame) : DataFrame de soumission.
    """

    # Création du DataFrame de soumission
    submission = pd.DataFrame({
        "Id"       : commune_ids,
        "Predicted": y_pred
    })

    # Sauvegarde en CSV
    submission.to_csv(filename, index=False)
    print(f"Soumission créée : {filename} ({len(submission)} lignes)")

    return submission