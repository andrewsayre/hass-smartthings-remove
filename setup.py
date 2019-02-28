"""hass_smartthings_remove"""

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join("README.md"), 'r') as fh:
    long_description = fh.read()

setup(name='hass_smartthings_remove',
      version="1.0.1",
      description='Utility that removes SmartApps created by the Home Assistant SmartThings integration.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/andrewsayre/hass-smartthings-remove',
      author='Andrew Sayre',
      author_email='andrew@sayre.net',
      license='MIT',
      packages=find_packages(),
      install_requires=['pysmartthings==0.6.3', 'aiohttp==3.5.4'],
      tests_require=['tox>=3.5.0,<4.0.0'],
      platforms=['any'],
      keywords="",
      zip_safe=False,
      entry_points={
          'console_scripts': ['hass_smartthings_remove=hass_smartthings_remove.remove:main'],
      },
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries",
          "Topic :: Home Automation",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          ])
