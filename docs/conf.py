import os
import sys
import django

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# -- Django setup ------------------------------------------------------------
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
# Mocking heavy dependencies that might not be available on RTD
autodoc_mock_imports = [
    'hail',
    'elasticsearch',
    'elasticsearch_dsl',
    'google',
    'google.auth',
    'social_django',
    'social_core',
    'anymail',
    'psycopg',
    'clickhouse_driver',
    'redis',
]

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
