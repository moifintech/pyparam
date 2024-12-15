from setuptools import setup

setup(
    name='pyparam',
    version="0.0.3",
    packages=['pyparam'],
    description='Param pos api python wrapper',
    url='https://github.com/erhan/pyparam',
    author='Erhan Bte',
    license='MIT',
    author_email='',
    install_requires=[
        'zeep'
    ],
    keywords='Param pos api python wrapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
