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
Le logiciel a été conçu en utilisant une architecture MVC (Modèle-Vue-Controlleur). Cette architecture permet de séparer les différentes responsabilités du logiciel en trois composants principaux : le Modèle, qui la logique des graphes et des algortihmes ; la Vue, qui est responsable de l'affichage des données obtenues par le modèle à l'utilisateur ; et le Contrôleur, qui fait le lien entre le Modèle et la Vue en gérant les interactions de l'utilisateur. 

Voici la composition du logiciel (cliquez):  
* [models](./sae_5_2/models/) : Contient les fichiers relatifs aux modèles, notemment [Node.py](./sae_5_2/models/Node.py) qui permet de créer des noeuds hexagonnaux (utilisation de coordonées hexagonales), où encore [Grid.py](./sae_5_2/models/Grid.py) qui permet de créer une grille et de joindre correctement les noeuds entre eux.  

* [views](./sae_5_2/views/) : Contient les fichiers qui concernent la vue. La vue principale étant [MainWindow.py](./sae_5_2/views/MainWindow.py), cette classe lie les autres vues contenues dans le répertoire et qui concernant les menus ou encore la grille.  

* [controllers](./sae_5_2/controllers/) : Contient les fichiers relatifs aux Controlleurs. Encore une fois, ce répertoire est composé d'un controleur principal [MainController.py](./sae_5_2/controllers/MainController.py) qui appelle les controlleurs des différents parcours.




### 3) Procédure



### 4) Utilisation