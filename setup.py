from setuptools import setup, find_packages

setup(
    name='tring',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'grpcio', 'scipy', 'numpy'
    ],
    author='',
    author_email='',
    description='grpc client for Tring Services',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/white-mastery-systems/tring-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
