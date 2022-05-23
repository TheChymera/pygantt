from setuptools import setup, find_packages

packages = find_packages(exclude=('pygantt.tests*'))

setup(
    name="pygantt",
    version="9999",
    description = " Simple Gantt Charts in Python ",
    author = "Horea Christian",
    author_email = "chr@chymera.eu",
    url = "https://github.com/TheChymera/pygantt",
    keywords = ["plotting", "productivity", "schedule", "gantt"],
    classifiers = [],
    install_requires = [],
    provides = ["pygantt"],
    packages = packages,
    include_package_data=True,
    extras_require = {
        },
    )
