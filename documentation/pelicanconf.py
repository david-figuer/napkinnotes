#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = ""
SITENAME = "Napkin Notes"
SITESUBTITLE = ""
SITEURL = "https://napkinnotes.es"
RELATIVE_URLS = False


PATH = "content"

# Regional Settings
TIMEZONE = "Europe/Madrid"
DATE_FORMATS = {
    "es": "%d de %B de %Y",
}
DEFAULT_LANG = "es"

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
MATH_JAX = {
    "auto_insert": True,
}
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
WITH_FUTURE_DATES = True
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"
EXPLORAR_URL = "explorar"
NOSOTROS_URL = "about"
# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
    ("X", "https://twitter.com/napkiinnotes", "Napkin Notes en X"),
)
# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra", "extra/_redirects", "code"]

"""EXTRA_PATH_METADATA = {
    "extra/custom-about.css": {"path": "theme/custom-about.css"},
    "extra/custom.css": {"path": "theme/css/custom.css"},
    "extra/_redirects": {"path": "_redirects"},
}"""

EXTRA_PATH_METADATA = {
    "extra/custom-about.css": {"path": "theme/custom-about.css"},
    "extra/custom.css": {"path": "theme/css/custom.css"},
}

if os.environ.get("CONTEXT") == "production":
    STATIC_PATHS.append("extra/robots.txt")
    EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}
else:
    STATIC_PATHS.append("extra/robots_deny.txt")
    EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "explorar", "404"]
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
X_USERNAME = "napkiinnotes"
X_PROFILE_URL = "https://twitter.com/napkiinnotes"
TWITTER_USERNAME = "napkiinnotes"
FEATURED_IMAGE = SITEURL + "/theme/images/nn_logo.png"

# Legal
SITE_LICENSE = """Contenido publicado bajo licencia <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Atribución 4.0 Internacional</a>."""
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
    "Duvier Suárez Fontanella": {
        "url": "https://produccioncientifica.usal.es/investigadores/819473/detalle",
        "role": "Creador, Desarrollador Web",
        "blurb": "Físico teórico y curioso incorregible, dedicado a rastrear las leyes secretas que gobiernan tanto al cosmos como a los detalles más triviales de la vida diaria. Sus textos buscan lo mismo que la antigua Fundación: preservar el conocimiento, iluminar lo oculto y demostrar que incluso en una servilleta puede comenzar una nueva era científica.",
        "avatar": "images/duvier.png",
    },
    "Gretel Quintero Angulo": {
        "url": "https://www.linkedin.com/in/gretel-quintero-angulo/?originalSubdomain=de",
        "role": "Editora",
        "blurb": "Gretel es científica de formación, escritora por placer y feminista por necesidad. Observa el mundo con la precisión de quien ha sido educada en el método científico y la sensibilidad de quien encuentra en la escritura una forma de interpretar lo cotidiano. Su trabajo combina pensamiento crítico y voz propia, explorando las estructuras —visibles e invisibles— que moldean nuestras vidas.",
        "avatar": "images/gretel.png",
    },
    "David Figueruelo Hernán": {
        "url": "https://inspirehep.net/authors/1869776?ui-citation-summary=true",
        "role": "Editor, Desarrollador Web",
        "blurb": "Doctor en cosmología que busca comprender el universo y el rol de la materia y energía oscuras en él. Interesado las ecuaciones y las preguntas fundamentales: qué significa entender en física y qué es  <strong>verdad</strong> al observar solo una fracción mínima del cosmos. Trabaja interpretando las pistas que el universo nos deja en forma de datos, intentando averiguar qué historias encajan con ellas y cuáles no. Financiación: Personal investigador doctor de la UPV/EHU (2024).",
        "avatar": "images/david.jpg",
    },
    "Gabriel Sánchez Pérez": {
        "url": "https://www.linkedin.com/in/gasape21/",
        "role": "Editor, Responsable de Redes Sociales",
        "blurb": "Gabriel es doctor en física teórica, un explorador obsesionado con la arquitectura matemática que sostiene el tejido del universo. En sus textos, se propone un desafío constante: traducir la complejidad de la física y la geometría a un lenguaje accesible, sin sacrificar ni un ápice de elegancia ni de rigor. Su enfoque busca desentrañar cómo las leyes fundamentales dan forma a nuestra realidad, convirtiendo abstracciones matemáticas en puentes hacia una comprensión profunda de la naturaleza.",
        "avatar": "images/gabriel.jpeg",
    },
    "Paz Albares Vicente": {
        "url": "https://portalcientifico.upm.es/es/ipublic/researcher/338845",
        "role": "Colaboradora",
        "blurb": "Paz es doctora en Física, especializada en Física Matemática, exploradora de ecuaciones no lineales y de los patrones que de ellas emergen donde menos se esperan. Modeliza fenómenos complejos e intenta descubrir y entender qué estructuras se esconden detrás, combinando la física con herramientas y el lenguaje de las matemáticas. De mente curiosa, está convencida de que tan importante es hacerse preguntas como buscar sus respuestas. Y a veces, todo comienza con una idea escrita en la cara de una servilleta.",
        "avatar": "images/paz.jpg",
    },
     "María Pérez Garrote": {
        "url": "https://produccioncientifica.usal.es/investigadores/1222882/detalle",
        "role": "Colaboradora",
        "blurb": "María es estudiante de doctorado en cosmología, y le apasiona intentar desentrañar los misterios del cosmos y de la vida en general. Su trabajo consiste en estudiar los ingredientes fundamentales que conforman el universo, y de qué manera interactúan para dar lugar a las formaciones de galaxias que observamos hoy en día. Sus textos aspiran a arrojar un poco de luz sobre ese sector todavía oscuro del universo, despertando la curiosidad y el pensamiento crítico en quienes se acercan a explorarlo.",
        "avatar": "images/maria.jpeg",
    },
     "Ruchika": {
        "url": "https://produccioncientifica.usal.es/investigadores/1999168/detalle",
        "role": "Colaboradora",
        "blurb": "Ruchika Ruchika Ruchika",
        "avatar": "images/gabriel.jpeg",
    },
}




COMMENTS_INTRO = "Comentarios"

APPLAUSE_BUTTON = True
DISPLAY_PAGES_ON_MENU = False
