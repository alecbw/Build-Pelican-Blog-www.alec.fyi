#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "AUTHORNAME"
SITENAME = "SITENAME"
# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ["uploads", "admin", "images"]

# The CMS Viewport Template
TEMPLATE_PAGES = {"admin/index.html": "admin/index.html"}

TIMEZONE = "America/Los_Angeles"
DEFAULT_LANG = "en"

PATH = "content"
STATIC_PATHS = ["uploads", "admin", "images"]

# Whether the home (index) page will paginate
DEFAULT_PAGINATION = False
# Overwrites the output directory (/output) when generating new files
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# path/to/theme/folder or name or installed via pelican-themes
# THEME = "themes/pelican-sober"

# Change to True if you want RSS
FEED_ALL_ATOM = False
FEED_ALL_RSS = False
