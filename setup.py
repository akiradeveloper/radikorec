#from distutils.core import setup
from setuptools import setup

setup(
	name = 'radikorec',
	version = '1.0',
	description = 'A Simple Radiko Recorder',
	author = 'Akira Hayakawa',
	author_email = 'ruby.wktk@gmail.com',
	scripts = [
		'bin/radikorec',
	],
	install_requires = [
		'argparse >= 1.2',
	],
)
