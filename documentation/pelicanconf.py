#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = ""
SITENAME = "Napkin Notes"
SITESUBTITLE = ""
SITEURL = ""
RELATIVE_URLS = True

PATH = "content"

# Regional Settings
TIMEZONE = "Asia/Karachi"
DATE_FORMATS = {"en": "%b %d, %Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
    
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "extract_toc",
    "liquid_tags.img",
    "liquid_tags.include_code",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
    "yaml_metadata",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
THEME = "../"
TYPOGRIFY = True
DEFAULT_PAGINATION = 10

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"
NOSOTROS_URL="about"

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (
    ("Github", "https://github.com/Pelican-Elegant/", "Elegant Github Repository"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
    (
        "Calendar",
        "https://github.com/Pelican-Elegant/elegant/milestones",
        "Elegant Project Roadmap",
    ),
)

# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra", "extra/_redirects", "code"]

EXTRA_PATH_METADATA = {
    "extra/custom-about.css": {"path": "theme/custom-about.css"},
    "extra/custom.css": {"path": "theme/css/custom.css"},
    "extra/_redirects": {"path": "_redirects"},
}

if os.environ.get("CONTEXT") == "production":
    STATIC_PATHS.append("extra/robots.txt")
    EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}
else:
    STATIC_PATHS.append("extra/robots_deny.txt")
    EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = False

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = "So what do you think? Did I miss something? Is any part unclear? Leave your comments below."

# Email Subscriptions
EMAIL_SUBSCRIPTION_LABEL = "Get New Release Alert"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Notify me"

FREELISTS_NAME = "oracle-l"
FREELISTS_FILTER = True

# SMO
TWITTER_USERNAME = ""
FEATURED_IMAGE = SITEURL + "/theme/images/nn_logo.png"

# Legal
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
HOSTED_ON = {"name": "Netlify", "url": "https://www.netlify.com/"}

# SEO
SITE_DESCRIPTION = (
    "Documentation of Elegant, a theme for Pelican, originally created by Talha Mansoor"
)

# Share links at bottom of articles
# Supported: twitter, facebook, hacker-news, reddit, linkedin, email
SHARE_LINKS = [("twitter", "Twitter"), ("facebook", "Facebook"), ("email", "Email")]

# Landing Page
PROJECTS_TITLE = "Related Projects"
PROJECTS = [
    {
        "name": "Elegant",
        "url": "https://github.com/Pelican-Elegant/elegant",
        "description": "Source code of Elegant theme",
    },
    {
        "name": "Issue Tracker",
        "url": "https://github.com/Pelican-Elegant/elegant/issues",
        "description": "Give your feedback, ask questions or report issues",
    },
    {
        "name": "Roadmap",
        "url": "https://github.com/Pelican-Elegant/elegant/milestones",
        "description": "See planned features and estimated release dates",
    },
    {
        "name": "Press Kit",
        "url": "https://github.com/Pelican-Elegant/elegant/tree/master/elegant-logo",
        "description": "Writing an article on Elegant? Get Elegant logo from here",
    },
    {
        "name": "onCrashReboot",
        "url": "https://www.oncrashreboot.com/",
        "description": "Home page of Elegant creator and lead developer",
    },
    {
        "name": "Pelican",
        "url": "https://github.com/getpelican/pelican/",
        "description": "Static site generator that powers Elegant",
    },
    {
        "name": "Pelican Plugins",
        "url": "https://github.com/getpelican/pelican-plugins",
        "description": "Collection of plugins for the Pelican static site generator",
    },
]

LANDING_PAGE_TITLE = "Napkin Notes"

AUTHORS = {
    "Duvier Suarez Fontanella": {
        "url": "https://produccioncientifica.usal.es/investigadores/819473/detalle",
        "role": "Creador",
        "blurb": "Físico teórico y curioso incorregible, dedicado a rastrear las leyes secretas que gobiernan tanto al cosmos como a los detalles más triviales de la vida diaria. Sus textos buscan lo mismo que la antigua Fundación: preservar el conocimiento, iluminar lo oculto y demostrar que incluso en una servilleta puede comenzar una nueva era científica.",
        "avatar": "images/duvier.jpeg",
    },
    "Gretel Quintero Angulo": {
        "url": "https://www.linkedin.com/in/gretel-quintero-angulo/?originalSubdomain=de",
        "role": "Editora",
        "blurb": "Gretel es científica de formación, escritora por placer y feminista por necesidad. Observa el mundo con la precisión de quien ha sido educada en el método científico y la sensibilidad de quien encuentra en la escritura una forma de interpretar lo cotidiano. Su trabajo combina pensamiento crítico y voz propia, explorando las estructuras —visibles e invisibles— que moldean nuestras vidas.",
        "avatar": "images/gretel.png",
    },
    "David Figueruelo": {
        "url": "https://produccioncientifica.usal.es/investigadores/148090/detalle",
        "role": "Editor",
        "blurb": "Investigador en cosmología que busca comprender el universo y el rol de la materia y energía oscuras en él. Interesado las ecuaciones y las preguntas fundamentales: qué significa entender en física y qué es *verdad* al observar solo una fracción mínima del cosmos. Trabaja interpretando las pistas que el universo nos deja en forma de datos, intentando averiguar qué historias encajan con ellas y cuáles no. Financiación: Personal investigador doctor de la UPV/EHU (2024).",
        "avatar": "images/david.jpg",
    },
    "Gabriel": {
        "url": "https://www.linkedin.com/in/gasape21/",
        "role": "Co-fundador · Diseño",
        "blurb": "Diseño y dirección visual del proyecto.",
        "avatar": "images/gabriel.jpeg",
    },
}

DISQUS_FILTER = True
UTTERANCES_FILTER = True
COMMENTBOX_FILTER = True
APPLAUSE_BUTTON = True
DISPLAY_PAGES_ON_MENU = False
