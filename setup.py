from setuptools import setup

setup(name='pyibge',
      version='0.1',
      description='Access data from IBGE (Brazilian Institute of Geography and Statistics) databases',
      url='https://github.com/renanbirck/pyibge',
      author='Renan Birck Pinheiro',
      author_email='renan.birck.pinheiro@gmail.com',
      license='MIT',
      packages=['pyibge'],
      zip_safe=False,
      install_requires=['requests'],
     )
