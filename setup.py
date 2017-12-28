#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('pybpodgui_plugin_oldformat/__init__.py', 'r') as fd:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
	                    fd.read(), re.MULTILINE).group(1)

if not version:
	raise RuntimeError('Cannot find version information')

setup(
	name='pybpod-gui-plugin-old-projects-format',
	version=version,
	description="""PyBpod GUI plugin for loading projects in the old format""",
	author='Ricardo Jorge Vieira Ribeiro',
	author_email='ricardojvr@gmail.com',
	license='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>',
	url='https://bitbucket.org/fchampalimaud/pybpod-gui-plugin-old-projects-format',

	include_package_data=True,
	packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),

	package_data={'pybpodgui_plugin_oldformat': [
		'resources/*.*',
	]
	},
)
