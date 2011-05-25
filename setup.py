# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("collective", "brasil", "vocab", "version.txt")).read().strip()

setup(name='collective.brasil.vocab',
      version=version,
      description="A Zope 3 vocabulary implementation of brasil.vocab",
      long_description=open(os.path.join("collective", "brasil", "vocab", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope brasil brazil vocabularies plone',
      author='Simples Consultoria <products@simplesconsultoria.com.br>',
      author_email='products@simplesconsultoria.com.br',
      url='https://bitbucket.org/simplesconsultoria/collective.brasil.vocab/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.brasil'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'brasil.vocab',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

