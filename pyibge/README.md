pyIBGE - a module to access IBGE data
-------------------------------------

This is a module to access data from IBGE (Brazilian Institute of Geography and Statistics). 
For now you need to know which table you're looking for and its parameters, this module is merely a way to make this access easier.

Such information can be found at http://api.sidra.ibge.gov.br/, by entering the table ID (which is available in the surveys - census, PNAD, IPCA, the agricultural surveys, the system of national accounts etc...).

It needs requests and lxml but nothing else beyond the standard Python. If you want to run tests you should install nose.

Future plans:
* A more user-friendly interface that allows you to specify which survey and which variable you want.
* Integration with pandas (for time series) and matplotlib (for direct graphing)

While I work for IBGE, this package is developed in (whatever remains of) my spare time and IBGE can't provide any help relating to it.