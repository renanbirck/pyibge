from setuptools import setup

setup(name='pyibge',
      version='0.1',
      description='Access data from IBGE (Brazilian Institute of Geography and Statistics) databases',
      url='https://github.com/renanbirck/pyibge',
      classifiers = [
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.6',
            'Topic :: Other/Nonlisted Topic',
            'Natural Language :: Portuguese (Brazilian)',
      ],
      author = 'Renan Birck Pinheiro',
      author_email = 'renan.birck.pinheiro@gmail.com',
      license='MIT',
      packages=['pyibge'],
      zip_safe=False,
      install_requires=['requests'],
      test_suite='nose.collector',
      tests_require=['nose'],
     )
