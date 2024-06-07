from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Wrapper in python per usufruire delle API di RE studenti di Axios Italia'

# Setting up
setup(
    name="SDAxiosAPI",
    version=VERSION,
    author="Invy55 (Marco)",
    author_email="<marco@invy55.win>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Invy55/AxiosStAPI",
    packages=find_packages(),
    install_requires=['pycryptodome', 'requests', 'pypybase64'],
    keywords=['python', 'axios', 'axios ita', 'axios italia', 'registro', 'elettronico', 'registro elettronico', 'api', 'wrapper', 'axios api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)