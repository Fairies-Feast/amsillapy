from setuptools import setup

from my_pip_package import __version__

setup(
    name='amsillapy',
    version=__version__,

    url='https://github.com/Fairies-Feast/amsillapy',
    author='Will Caesar',
    author_email='info@ffm.pw',

    py_modules=['requests'],
)
