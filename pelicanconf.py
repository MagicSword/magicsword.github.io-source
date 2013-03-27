# -*- coding: utf-8 -*-
AUTHOR = u'MagicSword'
SITENAME = u"Wondering"
SITEURL = 'http://magicsword.github.com'
TIMEZONE = "Asia/Taipei"



GITHUB_URL = 'http://github.com/magicsword/'
DISQUS_SITENAME = "magicsword-blog"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2013, 03, 01, 14, 01, 01)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('Disqus','http://magicsword-blog.disqus.com/'),)


SOCIAL = (('twitter', 'http://twitter.com/magicsword'),
          ('facecook', 'http://www.facebook.com/nero.miller'),
          ('github', 'http://github.com/magicsword'),)

# global metadata to all the contents
# DEFAULT_METADATA = (('Author', 'MagicSword'),)

# static paths will be copied under the same name
STATIC_PATHS = ["images", ]

# A list of files to copy from the source to the destination
# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
FILES_TO_COPY = (
                  ('extra/favicon.ico', 'favicon.ico'),
                  ('extra/robots.txt', 'robots.txt'),
                  ('extra/my-template-article.tmpl','my-template-article.tmpl')
                )
# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

#Theme
THEME = 'tuxlite_tbs'
