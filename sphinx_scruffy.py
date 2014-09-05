"""Plug-in for Sphinx to render "scruffy" diagrams."""
from os import path
import posixpath
import sys

try:
    from hashlib import sha1 as sha
except ImportError:  # pragma: no cover
    from sha import sha

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx.util.osutil import ensuredir
from sphinx.util.compat import Directive

# Scruffy modules.
import suml.common
import suml.suml2pic
import suml.yuml2dot


class ScruffyOptions(object):

    """Scruffy configuration class."""

    def __init__(self, kw):
        self.png = True
        self.shadow = False
        self.scruffy = True
        self.font = suml.common.defaultScruffyFont()
        for name, value in kw.iteritems():
            setattr(self, name, value)
        sys.stderr.write("Scruffy options: %r\n" % self.__dict__)

    def __getattr__(self, name):
        return None


class Scruffy(nodes.General, nodes.Element):

    """Scruffy node."""


class ScruffySimple(Directive):

    """Directive to insert Scruffy graphs (marked up as plain text)."""

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {
        'sequence': directives.flag,
        'class': directives.flag,
    }

    def run(self):
        node = Scruffy()
        node['code'] = '\n'.join(self.content)
        node['options'] = self.options
        return [node]


def render_scruffy(self, code, options, format, prefix='scruffy'):
    """Render scruffy code into a PNG output file.

    :param self: Sphinx main class object
    :param code: `string` of the code to be rendered
    :param options: `list` of rendering options
    :param format: `string` image format: png, jpg, etc
    :param prefix: `string` image file name prefix

    :return: `tuple` in form (<source image file name>, <output image file name>)
    """
    code = code.replace('\n', ',')
    hashkey = code.encode('utf-8') + str(options)
    image_filename = '%s-%s.%s' % (prefix, sha(hashkey).hexdigest(), format)
    assert hasattr(self.builder, 'imgpath'), "Only HTML output is supported!"
    source_image_file_name = posixpath.join(self.builder.imgpath, image_filename)
    output_image_file_name = path.join(self.builder.outdir, '_images', image_filename)
    if not path.isfile(output_image_file_name):
        ensuredir(path.dirname(output_image_file_name))
        with open(output_image_file_name, 'wb') as stream:
            scruffy_options = ScruffyOptions(dict((k, True) for k in options))
            if scruffy_options.sequence:
                suml.suml2pic.transform(code, stream, scruffy_options)
            else:
                suml.yuml2dot.transform(code, stream, scruffy_options)
    return source_image_file_name, output_image_file_name


def render_scruffy_html(self, node, code, options, prefix='scruffy', imgcls=None, alt=None):
    """Render scruffy node as html.

    :param self: Sphinx main class object
    :param node: Sphinx node object
    :param code: `string` of the code to be rendered
    :param options: `list` of rendering options
    :param prefix: `string` image file name prefix
    :param imgcls: `string` css class to add to <img> html tag
    :param alt: `string` alternative title for <img> html tag
    """
    format = 'png'
    try:
        fname, outfn = render_scruffy(self, code, options, format, prefix)
    except Exception as e:
        self.builder.warn('scruffy code %r: ' % code + str(e))
        raise nodes.SkipNode
    wrapper = 'p'
    self.body.append(self.starttag(node, wrapper, CLASS='Scruffy'))
    if alt is None:
        alt = node.get('alt', self.encode(code).strip())
    self.body.append('<img src="%s" alt="%s" %s/>\n' %
                     (fname, alt, imgcls and 'class="%s" ' % imgcls or ''))
    self.body.append('</%s>\n' % wrapper)
    raise nodes.SkipNode


def html_visit_scruffy(self, node):
    """Scruffy html rendering.

    :param self: Sphinx main class object
    :param node: Sphinx node object
    """
    render_scruffy_html(self, node, node['code'], node['options'])


def setup(app):
    """Shpinx plugin entry point.

    :param app: Sphinx application object
    """
    app.add_node(Scruffy,
                 html=(html_visit_scruffy, None))
    app.add_directive('scruffy', ScruffySimple)
