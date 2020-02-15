#!/usr/bin/env python
""" This example demonstrates that you need to run
'pip install .' in the main directory, before you
can do 'import streaming_projector_google_home' in a Python program

The from __future__ import below is to make this
code compatible with both Python 2 and 3
"""
from __future__ import print_function

try:
    import streaming_projector_google_home
    print("Succesfully imported streaming_projector_google_home!")
except ImportError:
    print("Could not import streaming_projector_google_home! Maybe you forgot to run 'pip install'")
