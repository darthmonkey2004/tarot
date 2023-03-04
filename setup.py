from distutils.core import setup

setup(name='tarot',
	version='1.0',
	description='tarot card example',
	author='Matt McClellan',
	author_email='darthmonkey2004@gmail.com',
	url='https://github.com/darthmonkey2004/tarot',
	packages=['tarot'],
	package_dir={'tarot': 'tarot'},
	data_files=['images.dat'],
	)
