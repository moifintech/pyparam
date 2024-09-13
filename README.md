from setuptools import setup, find_packages

setup(
    name='pyparam',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here, e.g.,
        # 'numpy>=1.18.0',
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here, e.g.,
            # 'pyparam=pyparam.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A parameter wrapper for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pyparam',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)# pyparam