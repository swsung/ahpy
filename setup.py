"""ahpy: python Analytic Hierarchy Process (AHP) library
"""

classifiers = """\
Development Status :: 3 - Alpha
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Libraries
Environment :: Any
Intended Audience :: Developers
"""

import sys
from distutils.core import setup
   
#from ez_setup import use_setuptools
#use_setuptools()

if sys.version_info < (2, 3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")

setup(name="ahpy",
      version="0.1",
      maintainer="Petri Savolainen",
      maintainer_email="petri.savolainen@iki.fi",
      platforms = ["win32", "unix"],
      packages = ["ahpy"],
      package_dir = {"ahpy": "lib"},
      description = doclines[0],
      classifiers = filter(None, classifiers.split("\n")),
      long_description = "\n".join(doclines[2:]),
)
