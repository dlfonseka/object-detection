"""Setup script for object_detection with TF2.0."""
import os
from setuptools import find_packages
from setuptools import setup
import subprocess

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)
os.symlink(".", "object_detection")
subprocess.call(["protoc object_detection/protos/*.proto --python_out=."], shell=True)
os.unlink("object_detection")

# Note: adding apache-beam to required packages causes conflict with
# tf-models-offical requirements. These packages request for incompatible
# oauth2client package.
REQUIRED_PACKAGES = ['pillow', 'lxml', 'matplotlib', 'Cython', 'contextlib2',
                     'six', 'pycocotools', 'scipy', 'pandas', 'tf-models-official']

setup(
    name='object_detection',
    version='0.2',
    install_requires=REQUIRED_PACKAGES + ['slim @ https://github.com/dlfonseka/object-detection/tarball/slim-v2'],
    packages=['object_detection.' + p for p in find_packages()] + ['object_detection'],
    package_dir={'object_detection': '.'},
    include_package_data=True,
    description='Tensorflow Object Detection Library',
    python_requires='>3.6',
)

