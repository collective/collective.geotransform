from setuptools import setup

version = '4.0.0.dev0'

setup(name='collective.geotransform',
      version=version,
      description="Gracefully email obfuscation for Plone",
      long_description=open("README.md").read() + "\n" +
                       open("CONTRIBUTORS.md").read() + "\n" +
                       open("CHANGES.md").read(),
      long_description_content_type="text/markdown",
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        ],
      keywords='geo email obfuscation Plone Zope',
      author='Victor Fernandez de Alba',
      author_email='sneridagh@gmail.com',
      url='https://github.com/collective/collective.geotransform',
      license='GPL',
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3.10',
      install_requires=[
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
