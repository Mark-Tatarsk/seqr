import os
import sys
from unittest.mock import MagicMock

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))

# -- Mocking modules for Read the Docs ---------------------------------------
MOCK_MODULES = [
    "django",
    "django.conf",
    "django.conf.settings",
    "django.db",
    "django.db.models",
    "django.contrib",
    "django.contrib.auth",
    "django.contrib.auth.models",
    "psycopg2",
    "hail",
    "elasticsearch",
    "elasticsearch_dsl",
    "google",
    "google.auth",
    "social_django",
    "social_core",
    "anymail",
    "django-anymail",
    "clickhouse_driver",
    "redis",
]

for mod in MOCK_MODULES:
    sys.modules[mod] = MagicMock()

# -- Project information -----------------------------------------------------
project = 'seqr'
copyright = '2026, seqr team'
author = 'seqr team'

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Autodoc configuration ---------------------------------------------------
autodoc_mock_imports = MOCK_MODULES

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
