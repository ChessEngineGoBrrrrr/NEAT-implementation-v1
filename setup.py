from setuptools import setup
from mypyc.build import mypycify

setup(
    name='import time.py',
    ext_modules=mypycify([
        "import time.py"
    ]),
)