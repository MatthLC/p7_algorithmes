# **Algorithmes v1.0.0**

## **Prérequis**

Ce projet est développé avec la version de Python 3.9, il est par conséquent recommandé d'installer cette version avant de continuer.


## **Initialisation de l'environnement**

### 1. Cloner la branche Main vers un répertoire local

- Créer un dossier sur votre ordinateur pour y disposer les fichiers présents sous GitHub

- Ouvrir un terminal (Ex: Windows PowerShell) et se positionner dans le dossier en question avec la commande cd, par exemple:

```
cd d:
cd -- "D:\mon_dossier"
```

### 2. Créer un environnement virtuel et installer les librairies à l'aide du fichier requirements.txt

- Créer l'environnement:


`python -m venv tournament`

- Activer l'nvironnement (L'environnement est activé une fois son nom affiché dans le terminal) : 

    - Windows:

    `tournament/Scripts/Activate.ps1` 

    - Inux et MacOS:  

    `source tournament/bin/activate`

- Installer les librairies : 

`pip install -r requirements.txt`


## **Lancement des programmes**

### 1. bruteforce.py :
Ce programme explore toutes les combinaisons possibles sur le fichier './database/forcebrute.csv' afin d'obtenir la meilleure solution d'actions à acheter pour une rentabilité optimale.

pour exécuter le programme, saisir la ligne suivante dans le terminal:
`py bruteforce.py`

Patienter jusqu'à l'affichage du résultat.

### 2. optimized.py :

Ce programme applique l'algorithme du sac à dos sur le fichier sélectionné dans le programme.
Pour modifier la source de données, il suffit de changer le nom du fichier de la variable 'my_data' dans le programme.

```
les fichiers de Sienna sont :
'./database/dataset1_Python+P7.csv'
'./database/dataset2_Python+P7.csv'
```

pour exécuter le programme, saisir la ligne suivante dans le terminal:
`py optimized.py`

Patienter jusqu'à l'affichage du résultat.
