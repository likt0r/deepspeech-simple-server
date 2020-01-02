import os, sys
try:
    from setuptools import setup, find_packages
    use_setuptools = True
except ImportError:
    from distutils.core import setup
    use_setuptools = False

try:
    with open('README.rst', 'rt') as readme:
        description = '\n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    description = ''

python_requires='>=3.5'
install_requires = [
    'deepspeech>=0.6.0',
]

setup(
    name="deepspeech-simple-server",
    version='1.1.0',
    url='https://github.com/likt0r/deepspeech-simple-server',
    license='MIT',
    description="simple server for mozilla deepspeech",
    long_description=description,
    author='Benjamin Werner',
    author_email='benjamin.werner@irie-web.de',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    scripts=['script/deepspeech-server'],
)
