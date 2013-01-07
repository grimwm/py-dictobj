from setuptools import setup
import os

def read(filename):
  fin = None
  data = None
  try:
    fin = open(filename)
    data = fin.read()
  finally:
    if fin is not None:
      fin.close()
  return data

setup(
  name='dictobj',
  version='0.3.1',
  author='William Grim',
  author_email='william@grimapps.com',
  url='https://github.com/grimwm/py-dictobj',
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
  description='A set of Python dictionary objects where keys can be accessed as instance attributes.',
  long_description=read('README.txt') if os.path.exists('README.txt') else '',
  py_modules=['dictobj'],
  test_suite='dictobj_test',
  )
