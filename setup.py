# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cai/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('cai/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='cai',
	version=version,
	description='Este modulo es donde se crearan los CAIs para los distintios tipos de documentos que maneja la empresa.',
	author='Frappe',
	author_email='gersoncaballero306@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
