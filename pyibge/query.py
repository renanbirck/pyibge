#!/usr/bin/env python3
#
# pyIBGE: A module to access data from the Brazilian Institute
# of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]

# Module where the main query functions are defined.
# Presently, this is a very, VERY thin wrapper arround the API.

import requests
from lxml import html

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
            

    def build_URL(self):
        """ Builds the URL for the queery. """
    
        CONSTANT_PART = "http://api.sidra.ibge.gov.br/values"
        VARIABLE_PART = '/t/' + str(self.table_ID)

        if self.params[0] != '/':
            VARIABLE_PART += '/'
       
        VARIABLE_PART += self.params
        
        return CONSTANT_PART + VARIABLE_PART
    
    def get_table_info(self):
        """ Gets the information (table title, variables, periods...)
        of the table. """

        self.table_info = {}

        URL = 'http://api.sidra.ibge.gov.br/desctabapi.aspx?c=' + str(self.table_ID)

        # Fortunately the guys at the IT department of IBGE had the good idea of using
        # descriptive names for id's and classes in the HTML. Then our work is really
        # simplified, we don't need to parse HTML.

        help_text = requests.get(URL)
        help_tree = html.fromstring(help_text.text)   # text instead of content
                                                      # avoids problems with charset

        try:
            unavailable_table = help_tree.xpath('//*[@id="lblMensagem"]/text()')[0]
        except:
            unavailable_table = ""
            pass
            
        if 'Tabela não possui dados de uso público' in unavailable_table:
           raise ValueError("This table is not available to the public.")
        

        
        table_title = help_tree.xpath('//*[@id="lblNomeTabela"]/text()')[0]
        self.table_info['table_name'] = table_title

        self.has_help = True    # We got the help information. Don't redo the query
                                # unless the table changes.
