import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="streaming_projector_google_home",
    version="0.0.1",
    author="Jordi Hernandez",
    author_email="jordihernandezlage@gmail.com",
    description=("An empty Python project"),
    license="Apache 2.0",
    keywords="Python",
    packages=['streaming_projector_google_home'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ]
)
