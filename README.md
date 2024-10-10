# Time Series Decomposer

Time Series Decomposer est une classe Python permettant de décomposer une série temporelle en ses trois composantes principales : tendance, saisonnalité et reste (remainder). Elle permet de comprendre la structure sous-jacente des données temporelles à travers une décomposition additive ou multiplicative. Cette approche est très utile pour analyser et modéliser des données temporelles.


## Installation

Clonez ce dépôt sur votre machine locale :

```bash
  git clone https://github.com/GuidePandore21/TimeSeriesDecomposer.git
```
    
## Features

La classe TimeSeriesDecomposer fournit les méthodes suivantes pour décomposer les séries temporelles :

- trend() : Calcule la tendance des données avec une fenêtre glissante.
- detrend(resultTrend) : Supprime la tendance des données pour obtenir le "DeTrend".
- seasonality() : Calcule la saisonnalité des données en divisant les données par segments saisonniers.
- remainder(trend, seasonality) : Calcule le reste (remainder) après suppression de la tendance et de la saisonnalité.
- decomposition() : Renvoie un dictionnaire avec toutes les composantes de la décomposition.
- displayResultDecomposition() : Affiche graphiquement les différentes composantes de la décomposition.


## Usage/Examples

La classe TimeSeriesDecomposer permet de réaliser une décomposition de série temporelle en fournissant les données, le type de décomposition (additive ou multiplicative), et la taille de la fenêtre de calcul.

```python
# Exemple de données
datas = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
type_decomposition = "additive"  # Ou "multiplicative"
window_size = 3

# Instancier la classe
decomposer = TimeSeriesDecomposer(datas, type_decomposition, window_size)

# Obtenir le résultat complet de la décomposition
result = decomposer.decomposition()

# Afficher les résultats graphiques
decomposer.displayResultDecomposition()
```
