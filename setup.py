from setuptools import find_packages, setup
from asgi_tortoise_orm.__version__ import __version__

setup(
    name="asgi-tortoise-orm",
    version=__version__,
    packages=find_packages(),
    install_requires=["tortoise-orm"],
    license="MIT License",
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
    url="https://github.com/erm/asgi-tortoise-orm",
    description="ASGI middleware for Tortoise ORM support",
)
