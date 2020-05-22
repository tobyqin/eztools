"""
Use this script to upload a pypi package, require below package:

    pip install setuptools -U
    pip install wheel -U
    pip install twine -U

"""
import os

from eztools.converters import to_int
from eztools.fileops import read_text, write_text

egg = 'dist'

if os.path.exists(egg):
    for f in os.listdir(egg):
        os.remove(os.path.join(egg, f))

# auto bump version

current_version = read_text('VERSION')
major, minor, revision = current_version.split('.')
revision_num = to_int(revision, regexp=True)
new_revision = revision.replace(str(revision_num), str(revision_num + 1))
new_version = f'{major}.{minor}.{new_revision}'
print(f'Bump version: {current_version} ==> {new_version}')
write_text('VERSION', new_version)

os.system('python setup.py sdist bdist_wheel')
os.system('twine upload dist/*')
