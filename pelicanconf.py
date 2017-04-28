#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Eugene Yurtsev'
SITENAME = u'Eugene Yurtsev'


PATH = 'content'

# Take advantage of the following defaults
# STATIC_SAVE_AS = '{path}'
# STATIC_URL = '{path}'
STATIC_PATHS = [
    'pages', 
    'img',
]

# DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "/home/eyurtsev/pelican-themes/Flex"
SITEURL = ''

# Blogroll
LINKS = (('Publications', 'https://scholar.google.com/citations?user=8ml2E2gAAAAJ&hl=en'),
        )

# Social widget
SOCIAL = (
    ('github', 'https://github.com/eyurtsev'),
)

SITELOGO = "/img/profile.jpeg"

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# put articles (posts) in blog/
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'    
TAG_SAVE_AS = 'blog/tag/{slug}.html'    
TAGS_URL = 'blog/tag/'  
TAGS_SAVE_AS = 'blog/tag/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
