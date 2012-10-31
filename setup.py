from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    install_requires=[
        'plone.app.dexterity[grok]',
    ],
    packages=find_packages(),
    name='dexterity_test',
)
