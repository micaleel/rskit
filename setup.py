try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re

version = re.search(
    '^__version__\s*=\s*"(.*)"', open("rskit/rskit.py").read(), re.M
).group(1)

with open("README.md", "rb") as f:
    description = f.read().decode("utf-8")

setup(
    name="rskit",
    packages=["rskit"],
    python_requires=">=3",
    entry_points={"console_scripts": ["rskit = rskit.rskit:main"]},
    version=version,
    description="Toolkit for recommender systems",
    long_description=description,
    long_description_content_type="text/markdown",
    author="Khalil Muhammad",
    author_email="micaleel@gmail.com",
    url="https://github.com/micaleel/rskit",
    license="MIT",
    keywords=[
        "personalization",
        "recommenders",
        "recommender systems",
    ],
    install_requires=["jupyter_client", "jupyter"],
)
