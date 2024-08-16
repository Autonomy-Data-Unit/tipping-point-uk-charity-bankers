from setuptools import find_packages, setup

setup(
    name="tipping_point_uk_charity_bankers",
    packages=find_packages(exclude=["tipping_point_uk_charity_bankers_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
