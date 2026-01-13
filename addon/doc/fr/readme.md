# Cursor Locator #

* Auteurs: Noelia Ruiz Martínez, Sergio Gómez Codina.

Cette extension permet de connaître la position du curseur du système par
rapport au début de la ligne en cours lors de la saisie pour ajouter du
texte dans des contrôles multilignes.

Cette fonctionnalité dépend de l'apparence visuelle des applications. Par
conséquent, vous devrez peut-être désactiver l'ajustement de ligne ou
configurer l'extension pour différents programmes.

## Paramètres Cursor Locator ##

Ce panneau est disponible dans le menu NVDA, sous-menu Préférences, boîte de
dialogue Paramètres.

Fournit les options suivantes:

* Annoncer longueur de ligne: Vous pouvez taper ou choisir une longueur de
  ligne (nombre de caractères entre 0 et 600), qui sera annoncé par une
  tonalité aigu lorsqu'il  est atteint. (La valeur par défaut est de 80
  caractères).
* Nombre maximum de bips pour la notification de début de ligne: Vous pouvez
  taper ou sélectionner une valeur comprise entre 0 et 600. La valeur par
  défaut est 0.
* Nombre maximum de bips pour la notification de fin de ligne: Vous pouvez
  taper ou sélectionner une valeur comprise entre 0 et 600. La valeur par
  défaut est 0.
* Hauteur du son pour le début de ligne: Vous pouvez taper ou sélectionner
  une valeur comprise entre 20 et 20000. (La valeur par défaut est de 400
  hertzs).
* Durée du son pour le début de ligne: Vous pouvez taper ou sélectionner une
  valeur comprise entre 20 et 2000. (La valeur par défaut est de 50
  millisecondes).
* Test du son pour le début de ligne: Appuyer sur ce bouton pour tester le
  son configuré pour le début de ligne.
* Hauteur du son pour  la fin de ligne: Vous pouvez taper ou sélectionner
  une valeur comprise entre 20 et 20000. (La valeur par défaut est de 1000
  hertzs).
* Durée du son pour la fin de ligne: Vous pouvez taper ou sélectionner une
  valeur comprise entre 20 et 2000. (La valeur par défaut est de 50
  millisecondes).
* Test du son pour la fin de ligne: Appuyer sur ce bouton pour tester le son
  configuré pour la fin de ligne.

## Commandes ##

Vous pouvez modifier les gestes associés aux commandes suivantes via le menu
NVDA, sous-menu Préférences, boîte de dialogue Gestes de commandes:

* NVDA+control+shift+l: Si possible, annonce la longueur de la ligne
  actuelle (catégorie Curseur système).
* Non assigné: Affiche la boîte de dialogue Paramètres Cursor Locator
  ((catégorie Configuration).

## Changements pour la version 3.0 ##


* Compatible avec NVDA 2023.1.


## Changements pour la version 2.0 ##

* Ajoutée la possibilité de répéter les notifications lorsqu'il  est atteint
  la fin et le début de ligne.
* Ajout de la prise en charge des documents Office et du Bloc-notes
  (Notepad) sous Windows 11.


## Changements pour la version 1.0 ##

* Première version

[[!tag dev stable]]
