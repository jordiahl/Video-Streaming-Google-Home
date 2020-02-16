#!/usr/bin/env python
""" This example demonstrates that you need to run
'pip install .' in the main directory, before you
can do 'import streamingProjectorGoogleHome' in a Python program

The from __future__ import below is to make this
code compatible with both Python 2 and 3
"""
from __future__ import print_function

try:
    import streamingProjectorGoogleHome
    print("Succesfully imported streamingProjectorGoogleHome!")
except ImportError:
    print("Could not import streamingProjectorGoogleHomestreaming_projector_google_home! Maybe you forgot to run 'pip install'")
