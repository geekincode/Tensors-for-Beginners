# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Tensors for Beginners'
copyright = '2026, geekincode'
author = 'geekincode'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_logo = '_static/logo.png'

html_static_path = ['_static']

html_css_files = [
    'css/style.css',
]

# -- 公式颜色配置
# -- Sphinx ≥ 4.0：默认使用 MathJax 3，用 mathjax3_config

mathjax3_config = {
    'tex': {
        'packages': {'[+]': ['xcolor']},
    }
}

