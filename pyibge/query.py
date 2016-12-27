#!/usr/bin/env python3
#
# pyIBGE: A module to access data from the Brazilian Institute
# of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]

# Module where the main query functions are defined.
# Presently, this is a very, VERY thin wrapper arround the API.

import requests

class IBGEQuery:
    """ The class that represents a query. 
    It receives the table ID and the parameters (available on the API documentation)."""

    def __init__(self, table_ID=None, params=None):
        if 0 < table_ID < 9999:
            self.table_ID = table_ID
        else:
            raise ValueError("Table ID must be between 0 and 9999.")

        if not params:
            raise ValueError("Need to specify what params you want.")      
        elif '/t/' in params:
            raise ValueError("Do not specify the 't' parameter in params, it is set by table_ID")
        else:
            self.params = params
            

    def URL(self):
        """ Builds the URL for the queery. """
    
        CONSTANT_PART = "http://api.sidra.ibge.gov.br/values"
        VARIABLE_PART = '/t/' + str(self.table_ID)

        if self.params[0] != '/':
            VARIABLE_PART += '/'
       
        VARIABLE_PART += self.params
        
        return CONSTANT_PART + VARIABLE_PART
    