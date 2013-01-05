from setuptools import setup
import os

def read(filename):
  with open(filename) as fin:
    return fin.read()

setup(
  name='dictobj',
  version='0.2.5',
  author='William Grim',
  author_email='william@grimapps.com',
  url='https://github.com/grimwm/py-dictobj',
  classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
  description='A set of Python dictionary objects where keys can be accessed as instnace attributes.',
  long_description=read('README.txt') if os.path.exists('README.txt') else '',
  py_modules=['dictobj'],
  test_suite='dictobj_test',
  )
