Title: FAQ (fr)
Date: 2011-09-01 12:00
Author: axx
Slug: faq-fr

Foire aux questions :

(Read in [English](/pages/faq.html "FAQ (en)"))

-   ***Quel est le langage de programmation utilisé par Memopol ?***  
    Python. Il y a également un peu de Javascript (web).  
    Si vous avez des compétences en webdesign, vous pouvez également
    nous aider à rendre Memopol plus beau et agréable à utiliser.
    
-   ***Utilisez vous un framework ou un CMS ?***  
    Oui, nous utilisons le framework
    [Django](http://www.djangoproject.com/ "Django Project").
    
-   ***Utilisez-vous un outil de travail collaboratif comme SVN, GIT,
    Bazaaar, Mercurial ou autre ?***  
    Oui, nous utilisons Git, et le projet est hébergé sur Github :
    [https://github.com/political-memory](https://github.com/political-memory).
	Le projet était sur Gitorious avant, et, Bram, le développeur principal, maintenait un miroir de ce dépôt sur [son compte Github](https://github.com/Psycojoker/memopol2).
	
-   ***Y a t-il du bug tracking ou d'autres fonctionnalités que je
    devrais connaître et utiliser en plus du partage de code source avec
    contrôle de version ?***  
    Le BTS (bug tracking system) est celui de Github, ici :
    [https://github.com/political-memory/political_memory/issues](https://github.com/political-memory/political_memory/issues)
    Pour faire un patch, un bon moyen est de cloner le dépôt puis de faire une pull request.
    Sinon, indiquez-nous l'adresse de votre dépôt.
    
-   ***Qui puis-je contacter pour participer au projet ?***  
    Vous pouvez vous venir vous présenter sur le salon IRC
    `\#lqdn-memopol` sur `irc://chat.freenode.net` où il vous sera fait bon
    accueil, ou envoyer un mail sur contact(at)memopol.org ou sur la mailing-list (lien plus bas).
    
-   ***Y a t-il un endroit virtuel où les développeurs se retrouvent ?
    Mumble ? IRC ?***  
    Les dévelopeurs se retrouvent sur IRC
    (`irc://irc.freenode.net\#lqdn-memopol`). Il n'y a pas de Mumble. Il y
    a une mailing list
    [http://laquadrature.net/cgi-bin/mailman/listinfo/mempol2](http://laquadrature.net/cgi-bin/mailman/listinfo/mempol2).
    Elle est actuellement peu utilisée, les développeurs utilisant
    principalement IRC.
    
-   ***Y a t-il déjà une analyse UML ou autre qui a été fait ? Ou
    n'importe quelle introduction technique au projet, liste des tâches
    à faire, description des interfaces, etc.***  
    Il n'y a actuellement pas d'UML. Il y a un schéma de la BDD ici
    [https://projets.lqdn.fr/attachments/download/7/graph.png](https://projets.lqdn.fr/attachments/download/7/graph.png).
    Il n'y a pas d'introduction technique, Memopol est un projet Django
    relativement standard, le code est simple, c'est principalement de
    l'affichage basé sur les class based generic views (une feature de
    Django). Chaque partie est correctement isolée.  
    Le schéma SQL est un peu plus complexe, par contre.
    
-   ***J'aimerais participer mais je manque de temps, avez-vous des
    tâches précises et détaillées à proposer ?***  
    Il n'y a malheureusement pas de tâches détaillées pour l'instant.
    Le projet avance trop vite et le nombre de codeurs est trop faible
    pour que l'investissement de les détailler soit rentable. Mais si il
    y a une demande il est tout à fait possible de la remplir. Le plus
    simple est de passer sur IRC et de demander à Bram ou à is_null.

