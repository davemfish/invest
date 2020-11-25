# -*- coding: utf-8 -*-
#
# InVEST 3 documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 12 11:08:28 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import ast
import importlib
import itertools
import logging
import os
import pkgutil
import sys
import warnings

import natcap.invest

logging.basicConfig()
LOGGER = logging.getLogger('__name__')


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
DOCS_SOURCE_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(DOCS_SOURCE_DIR, '..', '..', 'src'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
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
project = u'InVEST'
copyright = u'2019, The Natural Capital Project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import setuptools_scm
_version = setuptools_scm.get_version(
    root= os.path.join(DOCS_SOURCE_DIR, '..', '..'),
    version_scheme='post-release',
    local_scheme='node-and-date'
)
version = _version.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = _version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
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
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = False
#keep_warnings = True


# -- Options for HTML output ----------------------------------------------

import sphinx_rtd_theme
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/invest-logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.gif"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'InVEST3doc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'InVEST3.tex', u'InVEST 3 Documentation',
   u'The Natural Capital Project', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'invest', u'InVEST Documentation',
     [u'The Natural Capital Project'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'InVEST3', u'InVEST 3 Documentation',
   u'The Natural Capital Project', 'InVEST3', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# Specify the imports that must be mocked out in order to generate the docs.
autodoc_mock_imports = ['osgeo', 'osgeo.gdal', 'gdal']

# Mock class with attribute handling.  As suggested by:
# http://read-the-docs.readthedocs.io/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
from unittest.mock import MagicMock
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

# Any time we run a sphinx operation, also generate the API documentation.
# This should work OK, so long as the required modules (above) are sufficiently
# mocked up.
sys.modules.update((mod_name, Mock()) for mod_name in autodoc_mock_imports)

# mock the pygeoprocessing version to be whatever is in the natcap.invest
# __init__ file.
_invest_init = os.path.join(
    DOCS_SOURCE_DIR, '..', '..', 'src', 'natcap', 'invest',
    '__init__.py')
with open(_invest_init) as init_file:
    for line in init_file:
        if line.startswith('PYGEOPROCESSING_REQUIRED'):
            pgp_version = ast.literal_eval(line.split(' ')[-1].strip())
            sys.modules['pygeoprocessing'].__version__ = pgp_version

sys.modules['osgeo'].gdal.GetDriverCount.return_value = 1
sys.modules['osgeo.gdal'].GetDriverCount.return_value = 1
sys.modules['gdal'].GetDriverCount.return_value = 1

try:
    from natcap.invest import __version__
except ImportError:
    # If the package isn't installed, the __version__ attribute won't be
    # available.  Setting it anyways from the version from setuptools_scm.
    sys.modules['natcap.invest'].__version__ = _version

try:
    from sphinx import apidoc  # sphinx < 1.7
except ImportError:
    from sphinx.ext import apidoc  # sphinx >= 1.7
apidoc.main([
    '--force',
    '-o', os.path.join(DOCS_SOURCE_DIR, 'api'),
    os.path.join(DOCS_SOURCE_DIR, '..', '..', 'src', 'natcap')
])


MODEL_RST_TEMPLATE = """
.. _models:

=========================
InVEST Model Entry Points
=========================

All InVEST models share a consistent python API:

    1) The model has a function called ``execute`` that takes a single python
       dict (``"args"``) as its argument.
    2) This arguments dict contains an entry, ``'workspace_dir'``, which
       points to the folder on disk where all files created by the model
       should be saved.

Calling a model requires importing the model's execute function and then
calling the model with the correct parameters.  For example, if you were
to call the Carbon Storage and Sequestration model, your script might
include

.. code-block:: python

    import natcap.invest.carbon.carbon_combined
    args = {
        'workspace_dir': 'path/to/workspace'
        # Other arguments, as needed for Carbon.
    }

    natcap.invest.carbon.carbon_combined.execute(args)

For examples of scripts that could be created around a model run,
or multiple successive model runs, see :ref:`CreatingSamplePythonScripts`.


.. contents:: Available Models and Tools:
    :local:

"""

EXCLUDED_MODULES = [
    '_core',  # anything ending in '_core'
    '_example_model',
    'carbon_biophysical',
    'carbon_valuation',
    'coastal_vulnerability_post_processing',
    'usage_logger',
    'recmodel_server',
    'recmodel_workspace_fetcher',
]


def list_models(outfile):
    """List out all InVEST model entrypoints in RST.

    Writes a file with the list of models and their automodule documentation 
    directives for processing by sphinx.

    Arguments:
        outfile (string): The absolute path to write to.

    Returns:
        None

    """

    all_modules = {}
    iteration_args = {
        'path': natcap.invest.__path__,
        'prefix': 'natcap.invest.',
    }

    for _loader, name, _is_pkg in itertools.chain(
            pkgutil.walk_packages(**iteration_args),  # catch packages
            pkgutil.iter_modules(**iteration_args)):  # catch modules

        if any([name.endswith(x) for x in EXCLUDED_MODULES]):
            continue

        # Skip anything within the UI.
        if name.startswith('natcap.invest.ui'):
            continue

        try:
            module = importlib.import_module(name)
        except Exception:
            # If we encounter an exception when importing a module, log it
            # but continue.
            LOGGER.exception('Error importing %s', name)
            continue

        if not hasattr(module, 'execute'):
            continue

        try:
            module_title = module.execute.__doc__.strip().split('\n')[0]
            if module_title.endswith('.'):
                module_title = module_title[:-1]
        except AttributeError:
            module_title = None
        all_modules[name] = module_title

    LOGGER.debug('Writing models to file %s', outfile)

    with open(outfile, 'w') as models_rst:
        models_rst.write(MODEL_RST_TEMPLATE)

        for name, module_title in sorted(all_modules.items(),
                                         key=lambda x: x[1]):
            if module_title is None:
                warnings.warn('%s has no title' % name)
                module_title = 'unknown'

            models_rst.write((
                '{module_title}\n'
                '{underline}\n'
                '.. autofunction:: {modname}.execute\n\n').format(
                    module_title=module_title,
                    underline=''.join(['=']*len(module_title)),
                    modname=name
                )
            )


# list out all the models that conform to the InVEST API standard.
# write out to a file models.rst in the source dir (api-docs)
list_models(os.path.join(os.getcwd(), 'models.rst'))
