#from distutils.core import setup
from setuptools import setup

setup(
	name = 'radikorec',
	version = '1.0',
	description = 'A Simple Radiko/Radiru Recorder',
	author = 'Akira Hayakawa',
	author_email = 'ruby.wktk@gmail.com',
	url = 'https://github.com/akiradeveloper/radikorec',
	keywords = ['radiko', 'radiru', 'radio', 'recorder', 'NHK'],
	scripts = [
		'bin/radikorec',
	],
	platforms = ['POSIX'],
	package_dir = {'':'lib'},
	packages = [''],
	install_requires = [
		'argparse >= 1.2',
	],
	classifiers = [
		"Operating System :: POSIX :: Linux",	
		"Programming Language :: Python",
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"Topic :: Multimedia",
	],
)
