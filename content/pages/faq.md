Title: FAQ (en)
Date: 2011-11-22 16:35
Author: axx
Slug: faq

Frequently Asked Questions:

(Lire en [français](/pages/faq-fr.html "FAQ (fr)"))

-   ***What is the programming language used by Memopol?***  
    Python. There is also some Javascript for the web side of things.  
    If you have webdesign skills, you can help make Memopol better on
    the eyes and nicer to use.
    
-   ***Do you use a framework or a CMS?***  
    Yes, we use the
    [Django](http://www.djangoproject.com/ "Django Project") framework.
    
-   ***Do you use a collaborative work tool such as SVN, GIT, Bazaaar,
    Mercurial or something else?***  
    Yes, we use Git, and the project is now hosted on Github :
    [https://github.com/political-memory](https://github.com/political-memory).
    The projet was hosted on Gitorious before. Bram, the main developer, maintained a mirror repo on
    [his Github account](https://github.com/Psycojoker/memopol2).
    
-   ***Is there bug tracking or other functionalities I should know and
    use beyound source code sharing with revision control?***  
    The BTS (bug tracking system) used now is Github's one :
    [https://github.com/political-memory/political_memory/issues](https://github.com/political-memory/political_memory/issues).
    To send a patch, a good way is cloning github repository, and make a pull request. You can also tell us your
    repo's address.
    
-   ***Who should I get in touch with to take part in the project?***  
    You can come say hi on the IRC channel `\#lqdn-memopol` on 
    `irc://chat.freenode.net` where you should find a warm welcome, or
    simply get in touch by emailing contact(at)memopol.org, or the mailing list (link above).
    
-   ***Do the developers meet in a specific virtual space? Mumble?
    IRC?***  
    The developers meet on IRC (`irc://irc.freenode.net\#lqdn-memopol`).
    There is no Mumble server, there is a mailing list to which you can
    subscribe :
    [http://laquadrature.net/cgi-bin/mailman/listinfo/mempol2](http://laquadrature.net/cgi-bin/mailman/listinfo/mempol2).
    It is currently underused, as the developers mainly use IRC to
    communicate.
    
-   ***Huse there been a UML analyses done, or something similar? Or is
    there any technical introduction to the project, a task list, a
    description of interfaces, etc.?***  
    There is currently no UML. There is a database view here
    [https://projets.lqdn.fr/attachments/download/7/graph.png](https://projets.lqdn.fr/attachments/download/7/graph.png).
    There is no specific technical introduction, Memopol is a relatively
    standard Django project, the code is simple, it is mostly views
    based on class based generic views (a Django feature). Each part is
    properly isolated.  
	The SQL scheme is more complex on the other hand.
	
-   ***I'd like to help you but I don't have much time, to you have
    specific tasks I could work on?***  
    There are unfortunately no detailed tasks yet. The project is
    moving too fast with too little coders to make the time investment
    of detailing tasks worth it. But where there are needs, it is
    possible to help meet the. The easiest path of action is to drop by
    on IRC and ask Bram or is_null.
