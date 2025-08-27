Quelques tips pour aider à utiliser le terminal
-----------------------------------------------

- le terminal garde un historique des commandes tapées précédemment. Tu peux les naviguer en utilisant la flèche du haut.

- tu peux aussi chercher à travers l'historique en faisant: <CTRL-R> suivi par un terme à chercher. Par exemple, pour naviguer toutes les commandes qui contenaient le terme "postgres", tape <CTRL-R>, ensuite tape "postgres" et presse répétitivement <CTRL-R>, jusqu'à ce que tu retrouves la bonne commande. Quand tu la trouves presse sur <TAB>. Si tu veux annuler ta recherche tape <CTRL-G>.

- pour ignorer (annuler) une commande que tu étais en train de taper et simplement recommencer sur une autre ligne presse <CTRL-C>. C'est aussi la combinaison habituelle pour arrêter un programme qui est actif dans la fenêtre du terminal.

- Quand la fenêtre du terminal se remplit et que tu veux en effacer le contenu presse <CTRL-L>

Éditer les longues commandes
----------------------------
- les longues commandes peuvent être tapées sur la même ligne. Il peut être plus gérable de taper la commande en en écrivant des portions sur plusieurs lignes. Pour diviser une commande en plusieurs lignes, il faut terminer chaque ligne (sauf la dernière) par un backslash (le caractère \) suivi de <ENTER>. Il ne faut pas que le backslash soit suivi d'un espace ou d'un autre caractère sur la même ligne.

Par exemple, la commande

    $ docker image ls --all

peut être réécrite

    $ docker \
     image \
     ls --all

- Une alternative à écrire les longues commandes directement sur le terminal est de taper <CTRL-X CTRL-E> pour préparer d'abord la commande dans un éditeur de texte. Elle sera exécutée à la fermeture de l'éditeur.

- Il y a aussi un utilitaire appelé "fc" (fix command) qui permet d'éditer et exécuter les commandes les plus récentes:

    - pour lister les commandes récentes avec fc (noter le numéro identifiant chaque ligne)
    $ fc -l

    - éditer une des commande de la liste dans un éditeur 
    $ fc -r <identifiant de la commande>


Quelques tips pour la navigation de la ligne de commande
--------------------------------------------------------
- pour aller au début de la ligne <CTRL-A>

- pour aller à la fin de la ligne <CTRL-E>

- pour effacer tous les caractères de la position du curseur jusqu'à la fin de la ligne <CTRL-K>
- pour effacer tous les caractères de la position du curseur jusqu'au début de la ligne <CTRL-X> puis <BACKSPACE>.

    
