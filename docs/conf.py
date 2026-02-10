import os
import sys
from unittest.mock import MagicMock

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# -- Mocking modules for Read the Docs ---------------------------------------
# settings.py imports modules that are not available on RTD. 
# We mock them here BEFORE django.setup() is called.
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

MOCK_MODULES = [
    'google', 'google.auth', 'google.auth.transport', 'google.auth.transport.requests',
    'hail', 'elasticsearch', 'elasticsearch_dsl', 'social_django', 'social_core',
    'psycopg', 'clickhouse_driver', 'redis', 'corsheaders', 'hijack'
]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

# -- Django setup ------------------------------------------------------------
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# -- Project information -----------------------------------------------------
project = 'seqr'
copyright = '2026, seqr team'
author = 'seqr team'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# Build autosummary pages automatically
autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Autodoc configuration ---------------------------------------------------
# This allows autodoc to skip actually importing the mocked modules during documentation generation
autodoc_mock_imports = MOCK_MODULES

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
