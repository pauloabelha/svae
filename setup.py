from setuptools import setup
import numpy as np
from Cython.Build import cythonize

setup(
	name='svae',
    ext_modules=cythonize('**/*.pyx'),
    include_dirs=[np.get_include(),],
    packages=['svae']
)
