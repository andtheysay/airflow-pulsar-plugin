from setuptools import setup, find_packages

setup(
    name="airflow-pulsar-plugin",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "apache-airflow>=2.0.0",
        "pulsar-client>=2.7.0",
    ],
    author="andtheysay",
    author_email="andtheysay@protonmail.ch",
    description="An Apache Airflow plugin for Apache Pulsar integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andtheysay/airflow-pulsar-plugin",
    license="Apache License 2.0",
    classifiers=[
        "Framework :: Apache Airflow",
        "Framework :: Apache Airflow :: Plugin",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='>=3.6',
)