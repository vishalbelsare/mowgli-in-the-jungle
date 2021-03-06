from distutils.core import setup
from setuptools import find_packages

with open('requirements.txt', 'r') as f:
    install_requires = list()
    dependency_links = list()
    for line in f:
        re = line.strip()
        if re:
            if re.startswith('git+') or re.startswith('svn+') or re.startswith('hg+'):
                dependency_links.append(re)
            else:
                install_requires.append(re)

packages = find_packages()

setup(
    name='mowgli_framework',
    version="0.1.0",
    packages=packages,
    url='https://github.com/usc-isi-i2/mowgli-in-the-jungle',
    license='MIT',
    author='Filip Ilievski',
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links
)
