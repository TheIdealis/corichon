from setuptools import setup, Extension


def readme():
    with open('README.md') as f:
        return f.read()


PACKAGES = ['cornichon']

PACKAGE_DATA = {
    '.': ['README.md']
}

# import distutils.sysconfig

setup(name='cornichon',
      version='0.1',
      description='A way to save the data of a class in python',
      long_description=readme(),
      classifiers=[
          'Development Status :: 1 - Prealpha',
          'License :: ',
          'Programming Language :: Python :: 3.6',
      ],
      url='http://github.com/',
      author='Thomas Lettau',
      author_email='thomas_lettau@gmx.de',
      license='MIT',
      packages=PACKAGES,
      # install_requires=[
      #     'pickle'
      # ],
      package_data=PACKAGE_DATA,
      zip_safe=False)
