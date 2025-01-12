# SAE Semestre 5 : IN5SA01A - Méthodes d'optimisation

>Le logiciel développé dans le cadre d'une SAE (Situation d'Apprentissage et d'Evaluation) est un logiciel interactif qui permet de visualiser l'éxecution d'algorithmes de la théorie des graphes.
>
>Ce document présente brèvement le projet ainsi que son contenu et son fonctionnement.

## Sommaire
1. [But du logiciel](#1-but-du-logiciel)
2. [Description](#2-description)
3. [Procédure](#3-procédure)
4. [Utilisation](#4-utilisation)


### 1) But du logiciel
Le but de ce logiciel est de fournir un outil pédagogique permettant de mieux comprendre et visualiser les algorithmes de la théorie des graphes. Il doit permettre aux utilisateurs de suivre pas à pas l'exécution de ces algorithmes, facilitant ainsi l'apprentissage et la compréhension des concepts complexes associés aux graphes.  


***Chemin trouvé par A * sur notre logiciel***
![Algo A* de notre logiciel](./documents/image_but_du_logiciel.png)


### 2) Description  
Le logiciel a été conçu et développé en utilisant une architecture MVC (Modèle-Vue-Controlleur) avec le langage **Python**. Cette architecture permet de séparer les différentes responsabilités du logiciel en trois composants principaux : le Modèle, qui la logique des graphes et des algortihmes ; la Vue, qui est responsable de l'affichage des données obtenues par le modèle à l'utilisateur ; et le Contrôleur, qui fait le lien entre le Modèle et la Vue en gérant les interactions de l'utilisateur. 

Voici la composition du logiciel (cliquez):  
* [models](./sae_5_2/models/) : Contient les fichiers relatifs aux modèles, notemment [Node.py](./sae_5_2/models/Node.py) qui permet de créer des noeuds hexagonnaux (utilisation de coordonées hexagonales), où encore [Grid.py](./sae_5_2/models/Grid.py) qui permet de créer une grille et de joindre correctement les noeuds entre eux.  

* [views](./sae_5_2/views/) : Contient les fichiers qui concernent la vue. La vue principale étant [MainWindow.py](./sae_5_2/views/MainWindow.py), cette classe lie les autres vues contenues dans le répertoire et qui concernant les menus ou encore la grille.  

* [controllers](./sae_5_2/controllers/) : Contient les fichiers relatifs aux Controlleurs. Encore une fois, ce répertoire est composé d'un controleur principal [MainController.py](./sae_5_2/controllers/MainController.py) qui appelle les controlleurs des différents parcours.


### 3) Procédure  

Il faut tout d'abord cloner le projet en utilisant la commande suivante dans le répertoire voulu, ou bien directement dans votre IDE si vous préférez : 

```shell
git clone https://github.com/Neifko/sae_5_2.git
```

Afin d'executer le logiciel, il faut avoir les librairies suivantes d'installées dans son interpréteur python : 

* **Tkinter :** Bibliothèque standard de Python pour créer des interfaces graphiques.
* **Ctkinter :** Extension de Tkinter pour des widgets plus avancés.
* **heapq :** Module pour manipuler des tas (heaps) en Python.

Si ce n'est pas le cas, vous pouvez créer un environnement virtuel python et l'activer de la manière suivante (il faut ouvrir un terminal) :

**Sur Windows :**
```shell
python -m venv <nom_environnement>
<nom_environnement>/Scripts/activate
```

**Sur Linux/MacOS :** 
```shell
python3 -m venv <nom_environnement>
source <nom_environnement>/bin/activate
```

Si les étapes ont bien été suivies, le prompt devrait ressembler à cela : 

![Environnement Virtuel](./documents/image_procédure.png)

Finalement, il faut éxecuter la commande ci-dessous avec le fichier [requirements.yml](./config/requirements.yml) qui contient les dépendances listée un peu plus haut (il faut se déplacer dans le répertoire du fichier).

```shell
pip install -r requirements.yml
```

### 4) Utilisation