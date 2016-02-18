#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Memopol Team'
SITENAME = u'Memopol Project'
SITEURL = 'http://www.memopol.org/'
SITESUBTITLE= 'Bridging the gap between politics and citizens'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
LOCALE = u'en_EN.utf8'
DEFAULT_DATE_FORMAT = '%d/%m/%Y' 


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('La Quadrature du Net', 'https://www.laquadrature.net'),
         ('LQDN\'s Memopol Instance', 'http://lqdn.memopol.eu/'),
        )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/memopol2'),
         )

MORE =  (('Changing Democracy With Code: A Word From The Developers', '/pages/changing-democracy-with-code-a-word-from-the-developers.html'),
        ('FAQ (en)', '/pages/faq.html'),
         ('FAQ (fr)', '/pages/faq-fr.html'),
        )

DEFAULT_PAGINATION = 5

#menu
MENUITEMS = (('About', '/pages/about-memopol.html'),
            ('News', '/category/news.html'),
            ('Development diary','/category/development-diary.html'),
            ('Contribute', '/pages/contribute.html'),
            ('Download & install','/pages/download-install-instructions.html'),
            ('Contact','/pages/contact.html'),
            )
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

PLUGIN_PATHS = ["plugins", "/var/www/memopol-blog/plugins/"]
PLUGINS = ['pin_to_top']

#Theme
THEME = "/var/www/memopol-blog/foundation-memopol"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
