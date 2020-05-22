import os
import sys

import setuptools

# To prevent importing about and thereby breaking the coverage info we use this
# exec hack
about = {}
with open('eztools/__about__.py') as fp:
    exec(fp.read(), about)

if os.path.isfile('README.md'):
    long_description = open('README.md').read()
else:
    long_description = 'See http://pypi.python.org/pypi/eztools/'

needs_pytest = set(['ptr', 'pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

if __name__ == '__main__':
    setuptools.setup(
        name='eztools',
        version=about['__version__'],
        author=about['__author__'],
        author_email=about['__author_email__'],
        description=about['__description__'],
        url=about['__url__'],
        license='MIT',
        packages=setuptools.find_packages(),
        long_description=long_description,
        install_requires=['requests', 'arrow'],
        tests_require=['pytest'],
        setup_requires=[] + pytest_runner,
        classifiers=['License :: OSI Approved :: MIT License'],
    )
