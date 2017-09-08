# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


version = '1.0'
long_description = u'\n\n'.join([
    open("README.rst").read(),
    open("CHANGES.rst").read(),
])


setup(
    name='collective.gcs',
    version=version,
    description="Google Custom Search for Plone",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone google search',
    author='Johannes Raggam',
    author_email='raggam-nl@adm.at',
    url='https://github.com/collective/collective.gcs',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'plone.app.layout',
        'plone.app.registry',
        'plone.registry',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
