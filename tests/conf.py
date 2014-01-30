# Sphinx configuration to generate test documentation for the sphinx-scruffy sphinx plugin.
#
# Get the absolute paths of the docs/ directory and the repository root.
import os
import sys

script_name = os.path.abspath(__file__)
docs_directory = os.path.dirname(script_name)
build_directory = os.path.join(docs_directory, 'build')
media_directory = os.path.join(docs_directory, 'media')
repository = os.path.dirname(docs_directory)

# Make sure we can use toctree references
sys.path.insert(0, repository)

# Define the Sphinx configuration.
extensions = [
    'sphinx_scruffy',  # enable generated "scruffy" diagrams
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Test'
copyright = u'2013, Paylogic Developers'
version = '2.0'
exclude_trees = [build_directory]
show_authors = True
pygments_style = 'sphinx'
html_theme = 'default'
html_title = 'Documentation for the Test'
html_short_title = 'Test'
html_logo = os.path.join(media_directory, 'logo.png')
html_favicon = os.path.join(media_directory, 'favicon.ico')
html_static_path = [media_directory]
