### Démarrer un container pour postgres

    $ docker container run \
        --rm \
        --detach \
        --name db123 \ 
        --port 5432:5432 \ 
        --volume dbtest:/var/lib/postgresql/data \
        --env POSTGRES_PASSWORD=password \
        postgres

### Explications sur les options

    `--rm`
    
Par défaut, lorsqu'un container est arrêté, Docker le conserve, pour qu'il puisse être réutilisé plus tard. 
    L'option --rm (pour remove) instruit docker de supprimer le container aussitôt que celui ci est arrêté. 
    L'avantage de sauvegarder un container est qu'on n'a pas besoin de répéter la longue commande utilisée la première fois. On peut simplement spécifier le nom ou l'ID du container:

    $ docker container start <nom ou ID du container>
    
et le même container est redémarré.

Par contre, il arrive qu'on veuille juste essayer quelques configurations en passant et on ne veut pas que Docker les sauvegarde à chaque fois (ce qui force à plus tard les supprimer manuellement). Dans ce cas, spécifier --rm devient utile. Le container est utilisé normalement, et lorsqu'il est arrêté, il est automatiquement supprimé.

    --detach
    
Par défaut le container est lié à la fenêtre du terminal qui a été utilisée pour le démarrer. Si on a encore besoin d'utiliser la ligne de commande après le démarrage du container, on est obligé d'ouvrir une autre fenêtre de terminal. On doit aussi s'assurer que la fenêtre du container reste ouverte, car si on la ferme le container s'arrête.

L'option `--detach` (ou `-d`) permet au container de se détacher de la fenêtre et de fonctionner en arrière plan. Il devient donc possible de continuer d'interagir avec le terminal après le démarrage du container, et même de fermer la fenêtre du terminal sans affecter le container. Pour arrêter un container qui tourne en arrière plan, il faut utiliser la commande (d'une quelconque fenêtre de terminal).

    $ docker container stop <nom ou ID du container>

    `--name <nom du container>` 
    
On peut utiliser cette option pour spécifier soit même le nom du container, sinon, docker lui même donnera un nom.

    --port <port externe>:<port interne>

Cette option spécifie comment communiquer de l'extérieur du container avec Postgresql qui tourne dans le container. Par défaut Postgresql est configuré pour écouter sur le port 5432 de la machine où il est installé, dans le cas présent, le port 5432 d'un container (le port interne). Les ports du container sont complètement invisibles au monde externe. Si on veut que des applications externes puissent communiquer avec les applications internes, il faut créer des ponts entre le container et le monde externe. Une approche est de créer des correspondances entre les ports internes et les ports externes (ceux à qui les applications externes peuvent parler). Ça consiste simplement à demander à Docker d'écouter certains ports externes et de transmettre tout ce qu'il reçoit aux ports internes, tel qu'il est spécifié. Dans le cas présent, 5432:5432 indique à Docker d'écouter sur le port 5432 de la machine et de retransmettre toutes les communications vers le port 5432 du container, qui lui est écouté de l'interieur par Postgresql. De cette manière une application cliente peut être configurée normalement pour se connecter au port (externe) 5432 de la machine et Docker fera le relais au port 5432 interne du container. Le port externe choisi ne doit juste pas déjà être utilisé par une autre application ou être assigné à un autre container. Le port interne dépend de comment Postgresql est configuré.

    --volume dbtest:/var/lib/postgresql/data 

Le container tourne en mémoire et est éphémère. Son système de fichier lui aussi fonctionne en mémoire. Lorsqu'il est arrêté, tout ce qui a été créé pendant la session active est purgé de la mémoire. Si on veut pouvoir conserver des changements il faut instruire Docker de créer un espace sur le disque dur où il copiera tous les changements apportés à un certain répertoire executés dans le container. Dans le cas présent, Postgresql est configuré par défaut pour placer les fichiers de sa base de données au répertoire `/var/lib/postgresql/data` du système où il est installé. Pour conserver ces changements, Docker connecte un espace sur le disque dur avec le répertoire de Postgresql dans le container. Cet espace géré par Docker est appelé un volume. L'administration des volumes se fait par le client docker (e.g. docker volume ls)

    --env POSTGRES_PASSWORD=password 

Cette option indique un mot de passe initial à utiliser pendant l'installation de Postgresql dans le container.
