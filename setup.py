from os.path import abspath, dirname, join

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class ToxTestCommand(TestCommand):
    """Test command which runs tox under the hood."""

    def finalize_options(self):
        """Add options to the test runner (tox)."""
        TestCommand.finalize_options(self)
        self.test_args = ['--recreate']
        self.test_suite = True

    def run_tests(self):
        """Invoke the test runner (tox)."""
        #import here, cause outside the eggs aren't loaded
        import detox.main
        errno = detox.main.main(self.test_args)
        sys.exit(errno)

long_description = []

for text_file in ['README.rst', 'CHANGES.rst']:
    with open(join(dirname(abspath(__file__)), text_file), 'r') as f:
        long_description.append(f.read())

setup(
    name='sphinx_scruffy',
    version='0.2',
    description='Plug-in for Sphinx to render "scruffy" diagrams.',
    long_description='\n'.join(long_description),
    author='Paylogic International',
    author_email='developers@paylogic.com',
    license='MIT',
    install_requires=[
        'sphinx',
        'scruffy',
        'Pillow'
    ],
    packages=find_packages(exclude=['ez_setup']),
    tests_require=['detox'],
    cmdclass={'test': ToxTestCommand},
    keywords='sphinx scruffy diagrams documentation',
)
