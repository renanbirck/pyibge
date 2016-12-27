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
                 variables='allxp', level='n1', sublevel='all',
                 classification=None, **kwargs):
        if 0 < table_ID < 9999:
            self.table_ID = table_ID
        else:
            raise ValueError("Table ID must be between 0 and 9999.")


        self.period = period
        self.variables = variables
        self.level = level
        self.classification = classification

        # kwargs are used for defining the formatting.

        # The 'f' parameter.
        try:
            self.result_format = kwargs['format'].lower
        except KeyError:    # No result format was given
            self.result_format = 'a'

        if self.result_format and self.result_format not in ['c', 'n', 'u', 'a']:
            raise ValueError("The result format must be one of 'c', 'n', 'u' or 'a'.")
        
        # The 'd' parameter.

        try:
            self.digits = kwargs['num_digits'].lower
        except KeyError:
            self.digits = 's'

        if self.digits and self.digits not in ['s', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            raise ValueError("The digits must be 0-9, 'm' (maximum digits available) or 's' (default).")

        # The 'h' parameter

        try:
            self.header = kwargs['get_header']
        except KeyError:
            self.header = True
