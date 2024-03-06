from setuptools import setup, find_packages

setup(
    name='Json-Encoder-Decoder',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'json-encoder-decoder = main.main:main',
        ],
    },
)