from setuptools import setup
import markdown2

def markdown(filename):
  md = markdown2.Markdown()
  with open(filename) as fin:
    return md.convert(fin.read())

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
  long_description=markdown('README.md'),
  py_modules=['dictobj'],
  test_suite='dictobj_test'
  )
