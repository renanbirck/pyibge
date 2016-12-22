#!/usr/bin/env python3
#
# pyIBGE: A module to access data from the Brazilian Institute
# of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]

# Module where the main query functions are defined.
# Presently, this is a very, VERY thin wrapper arround the API.

import requests

class IBGEQuery():
    """ The class that represents a query. """

    def __init__(self, table_ID=None, period='last',
                 variables='allxp'):
        if 0 < table_ID < 9999:
            self.table_ID = table_ID
        else:
            raise ValueError("Table ID must be between 0 and 9999.")
        pass

        self.period = period
        self.variables = variables

    pass