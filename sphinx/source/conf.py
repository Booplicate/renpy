# -*- coding: utf-8 -*-
#
# The Ren'Py Visual Novel Engine documentation build configuration file, created by
# sphinx-quickstart on Tue Jun 15 17:02:51 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
# import sphinx_rtd_theme
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'renpydoc',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Ren\'Py Visual Novel Engine'
copyright = u'2012-{}, Tom Rothamel'.format(datetime.date.today().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

sys.path.insert(0, '../..')
import renpy

version = ".".join(str(i) for i in renpy.version_tuple[:3])
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [ ]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'sphinxdoc'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = { }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path() + [ '.' ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Ren'Py Documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "navbar-logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

html_baseurl = "https://www.renpy.org/doc/html/"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
# html_sidebars = { '**': ['localtoc.html' ] }

html_css_files = [
    'custom.css',
]

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

html_context = {
  'display_github': True,
  'github_user': 'renpy',
  'github_repo': 'renpy',
  'github_version': 'master/sphinx/source/',
}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

html_permalinks = True
html_permalinks_icon = " link"

locale_dirs = ["locale/"]


latex_documents = [
    ('index', 'all.tex', u'Ren\'Py Visual Novel Engine Reference Manual', u'', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "logo.png"


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'The Ren\'Py Visual Novel Engine'
epub_author = u''
epub_publisher = u''
epub_copyright = copyright


# -- More options --------------------------------------------------------------

highlight_language = "renpy"

extlinks = {
    'lpbug': (
        'https://bugs.launchpad.net/renpy/+bug/%s',
        'launchpad bug %s'),
    'ghbug': (
       'https://github.com/renpy/renpy/issues/%s',
        'github bug %s'),
    }

rst_prolog = """\
.. |PGS4A| replace:: RAPT
.. |PGS4A_URL| replace:: http://www.renpy.org/dl/android/
"""

def setup(app):
    app.add_config_value('is_renpy', '', True)
    app.add_config_value('renpy_figures', '', True)

is_renpy = "renpy"
renpy_figures = ("figures" if ("RENPY_NO_FIGURES" not in os.environ) else '')
