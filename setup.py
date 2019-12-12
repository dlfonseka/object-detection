from setuptools import setup, find_packages
import os

setup(
    name='object-detection',
    version='0.0.1',
    description='Tensorflow object detection API',
    package_dir={'object_detection': '.'},
    packages=['object_detection.' + p for p in find_packages()],
    install_requires=[
        'tensorflow>=1.12.0',
        'Cython',
        'contextlib2',
        'pillow',
        'lxml',
        'jupyter',
        'matplotlib',
        'slim @ git+https://github.com/autognc/object-detection@slim'
    ])
