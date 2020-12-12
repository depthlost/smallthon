from distutils.core import setup
setup(
  name = 'smallthon',
  packages = ['smallthon'],
  version = '1.1',
  license='GPLv3',
  description = 'This library adds functionality to standard python collections',
  author = 'Nehuen Pereyra & Iyael Pereyra',
  author_email = 'devflags@gmail.com',
  url = 'https://github.com/depthlost/smallthon',
  download_url = 'https://github.com/depthlost/smallthon/archive/v1.1.tar.gz',
  keywords = ['COLLECTION', 'OOP', 'LIST'],
  install_requires=[
          'forbiddenfruit==0.1.3'
      ],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3.6',
  ],
)
