from setuptools import setup, find_packages


setup(name='loniapi',
      version='0.1',
      description='Package to make calls to the LONI API',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
      ],
      keywords='sage bionetworks ida file downloads',
      url='https://github.com/Sage-Bionetworks/loni-api',
      author='Hieu Do',
      author_email='hieu.do@sagebionetworks.org',
      license='MIT',
      packages= find_packages(include=['loniapi', 'loniapi.*']),
      install_requires=[
          'requests',
      ],
      zip_safe=False)
