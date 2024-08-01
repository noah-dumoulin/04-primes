# Nombres premiers

Un [nombre premier](https://en.wikipedia.org/wiki/Prime_number) est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs. Ces deux diviseurs sont 1 et le nombre considéré. L'objectif est d'écrire du code qui permet de vérifier si un nombre est premier ou pas.

Le fichier ``primes.py`` contient :

- une fonction secondaire ``isprime()`` qui a pour but de vérifier si un entier est un nombre premier ou pas. 
  
  - elle prend en argument un nombre entier ``p`` ;
  - et retourne un booléen exprimant la vérité de « ``p`` est un nombre premier ». 
  
- la fonction principale ``main()`` qui fait quelques appels à la fonction secondaire permettant de vérifier son bon fonctionnement .

## To do

1️⃣ Ecrire le code de la fonction secondaire.

2️⃣ Ecrire quelques appels à la fonction secondaire dans ``main()``.

3️⃣ Exécuter le programme depuis le terminal

    $ python primes.py

Répéter le cycle 1️⃣ 2️⃣ 3️⃣ jusqu'à atteinte des objectifs.

4️⃣ Une fois le code fonctionnel, le soumettre aux tests unitaires. Le grade obtenu est le pourcentage de tests réussis. 

    $ pytest

5️⃣ Lorsque le grade est satisfaisant, soumettre le travail pour évaluation

    $ git pull
    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.

## Environnement de travail

Vous devez être connecté sur un compte [GitHub](https://www.github.com). Vous avez reçu un lien [GitHub Classroom](https://classroom.github.com) correspondant à cet exercice. En acceptant cet exercice, deux ressources distintes 🅰 et 🅱 ont été générées dans le cloud.

🅰 un [repo GitHub](https://docs.github.com/fr/repositories/creating-and-managing-repositories/about-repositories) dont l'URL générique est ``https://github.com/[CLASSE]/[ASSIGNMENT-YOUR_GITHUB_NAME]``. C'est un référentiel qui contient l’ensemble du code, et des fichiers associés à cet exercice. A l'état initial, il contient le starter code. 

🅱 un [codespace](https://docs.github.com/en/codespaces/overview) dont l'URL générique est ``https://[CODESPACE_NAME].github.dev``. C'est un environnement de développement [Visual Studio Code](https://code.visualstudio.com/) hébergé dans le cloud. Ce codespace a été initialisé avec le contenu du repo 🅰. C'est ici que l'on doit :

- écrire le code
- l'exécuter
- le tester
- soumettre son travail

Ces deux ressources 🅰 et 🅱 doivent être ouvertes simultanément dans un navigateur. Le développement se fait dans le ``codespace`` 🅱.

> [!NOTE]
> L'opération 5️⃣ permet :
> - de synchroniser le codespace 🅱 et le repo 🅰
> - d'observer les détails de l'évaluation du travail dans l'onglet ``Actions`` du repo 🅰.


