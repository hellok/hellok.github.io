#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'hellok'
SITENAME = u'helloworld'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'


GITHUB_URL = 'http://github.com/hellok/hellok.github.io'


#ARTICLE_URL = ('{slug}')
ARTICLE_SAVE_AS = ('{slug}.html')
PAGE_URL = ('{slug}')
PAGE_SAVE_AS = ('{slug}.html')
AUTHOR_URL = ('author/{name}')
TAG_URL = ('tag/{name}/')


THEME =('bootstrap')

#ARTICLE_URL = ('{slug}')
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


STATIC_PATHS = ['images', 'pdfs','css','theme','feeds','category','author']

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('maps', 'http://maps.google.com'),)

# Social widget
SOCIAL = (('github', 'http://github.com/hellok'),
          ('sinaapp', 'http://repro.sinaapp.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
