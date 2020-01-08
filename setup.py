from setuptools import setup, find_packages
import os
import subprocess

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)
if not os.path.exists("object_detection"):
    os.symlink(".", "object_detection")
subprocess.call(["protoc object_detection/protos/*.proto --python_out=."], shell=True)
os.unlink("object_detection")

setup(
    name='object-detection',
    version='0.0.1',
    description='Tensorflow object detection API',
    package_dir={'object_detection': '.'},
    packages=['object_detection.' + p for p in find_packages()] + ['object_detection'],
    install_requires=[
        'Cython',
        'contextlib2',
        'pillow',
        'lxml',
        'jupyter',
        'matplotlib',
        'slim @ https://github.com/autognc/object-detection/tarball/slim'
    ])
