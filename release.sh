#!/bin/bash

# Run build
pandoc README.md -w rst -o README.txt
python setup.py sdist upload

# Do cleanup
rm -f README.txt
rm -rf dist
rm -rf dictobj.egg-info
rm -rf __pycache__
rm -f *.pyc
