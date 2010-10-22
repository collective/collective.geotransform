from setuptools import setup, find_packages
import os

version = '1.0a1'

setup(name='collective.geotransform',
      version=version,
      description="Gracefully email obfuscation for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='geo email obfuscation Plone Zope',
      author='Victor Fernandez de Alba',
      author_email='sneridagh@gmail.com',
      url='http://svn.plone.org/svn/collective/collective.geotransform',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.transformchain',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
