import os
import sys
from unittest.mock import MagicMock

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))

# -- Mocking modules for Read the Docs ---------------------------------------
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

def mock_package(name):
    m = Mock()
    m.__path__ = []
    sys.modules[name] = m
    return m

# Mocking the package tree to avoid "is not a package" errors
packages = [
    "django", "django.conf", "django.db", "django.db.models", "django.core", 
    "django.core.wsgi", "django.core.management", "django.contrib", "django.contrib.auth",
    "google", "google.auth", "google.auth.transport",
    "elasticsearch", "elasticsearch_dsl", "hail"
]

for pkg in packages:
    mock_package(pkg)

MOCK_MODULES = [
    "django.conf.settings",
    "django.db.models.query",
    "django.db.models.expressions",
    "django.contrib.auth.models",
    "psycopg2",
    "google.auth.transport.requests",
    "social_django",
    "social_core",
    "anymail",
    "django-anymail",
    "clickhouse_driver",
    "redis",
    "corsheaders",
    "hijack",
]

for mod in MOCK_MODULES:
    sys.modules[mod] = MagicMock()

# Mock Django version to avoid comparison errors
import django
django.VERSION = (4, 2, 0, 'final', 0)
django.get_version = lambda: "4.2"

# -- Project information -----------------------------------------------------
project = 'seqr'
copyright = '2026, seqr team'
author = 'seqr team'

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Autodoc configuration ---------------------------------------------------
autodoc_mock_imports = MOCK_MODULES + packages

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
