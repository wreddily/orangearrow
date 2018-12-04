from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="orangearrow",
    description="A Python Library for interacting with the Amazon Product Advertising API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="v0.9.6",
    author='Joe Wilson',
    license='Apache2',
    url="https://github.com/wreddily/orangearrow",
    packages=['orangearrow'],
    install_requires=[
        "requests==2.20.0",
        "xmltodict==0.11.0",
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ]
)
