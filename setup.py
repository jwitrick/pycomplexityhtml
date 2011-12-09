#!/usr/bin/python

from distutils.core import setup

setup (name = "PyComplexityHTML",
       version = "PYCOMPLEXITYHTML_VERSION",
       author = "Justin Witrick",
       author_email = "justin.witrick@rackspace.com",
       description = "This will output McCabe complexity in a HTML format that can be read by CI machines (Hudson, Jenkins)",
       url = "",
       packages = ['PyComplexityHTML'],
       scripts = ['pycomplexityhtml']
)
