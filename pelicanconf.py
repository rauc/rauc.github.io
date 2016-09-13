#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pengutronix'
SITENAME = u'RAUC'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'}
        }

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = "theme-rauc"

GITHUB_URL = "http://github.com/rauc/rauc"
TWITTER_USERNAME = "rauc_updater"

#DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Download', 'pages/download.html'),
    ('Documentation', 'rauc.readthedocs.io'),
    ('Media', 'pages/media.html'),
    ('Blog', 'www.pengutronix.de/en/tags/rauc.html'),
    ('Support', 'pages/support.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
