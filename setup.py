from setuptools import setup, find_packages

setup(
    name='adaptable_fdm',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy'],
    description='Modular simulation library',
    author='Pablo Diez Silva',
    author_email='pablodiezsilva@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
