from setuptools import setup, find_packages
import os

version = '2.0a1'

setup(name='collective.geotransform',
      version=version,
      description="Gracefully email obfuscation for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        ],
      keywords='geo email obfuscation Plone Zope',
      author='Victor Fernandez de Alba',
      author_email='sneridagh@gmail.com',
      url='https://github.com/collective/collective.geotransform',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'plone.transformchain',
          'beautifulsoup4',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.contenttypes',
              'plone.app.robotframework',
              'plone.app.testing',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
