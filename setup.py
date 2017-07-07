from setuptools import setup

setup(name='paragon',
      version='0.0.1',
      description='',
      author='Andrew Barisser',
      author_email='barisser@protonmail.com',
      license='MIT',
      packages=['paragon'],
      install_requires=[
          'boto',
          'networkx',
          'sqlalchemy'
      ],
      tests_require=['pylint', 'pytest', 'pytest-cov']
      )
