from setuptools import setup

setup(
  name='dictobj',
  version='0.2.4',
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
  py_modules=['dictobj'],
  test_suite='dictobj_test'
  )
