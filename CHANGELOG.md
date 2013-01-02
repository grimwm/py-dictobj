v0.2.4
======
Properly formatted README.md and added some details about how
to contribute to this project.

Added doctests to this project since the examples actually do
work as valid tests taht can be run.  Found some bugs, resolved
them, and added everything to the automated testing suite.

Changed CHANGELOG to CHANGELOG.md.

v0.2.3
======
Adding the source code URL to the README so that it's easier
for people to find and help contribute.

v0.2.2
======
Changelog started and prior versions added to this file.

Removed some code from MutableDictionaryObject.__setattr__
that is no longer needed now that DictionaryObject.__init__
properly handles initialization of __dict__ when passed in a
DictionaryObject.

v0.2.1
======
Improved the thoroughness of the documentation.

Added a description for PyPi.

v0.2
====
Fixed equality operators and the comparison method.

Fixed object copying when passing in another DictionaryObject.

Fixed handling of default values upon __init__.

Added __setstate__ / __getstate__ so pickle now works correctly
with the classes.

Fixed error reporting on exceptions.

Improved __repr__ so it gives a proper string represenation of
our classes so they can later be eval'd.

Added more unit tests:
 - test_pickle
 - test_copy
 - more equality tests

Added more examples to the documentation.

v0.1.1
======
First release.