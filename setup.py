import setuptools
from setuptools import setup

setup(
    name="cp-hec-api-sdk",
    version="1.0",
    author="Travis Lockman",
    license='Apache 2.0',
    description="Check Point HEC API SDK",
    long_description="Check Point Harmony Email and Collaboration SDK",
    long_description_content_type="text/plain",
    url="https://github.com/travislockman/cp_hec_api_python_sdk",
    py_modules=["cphec.cp_hec_api"],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]

)
