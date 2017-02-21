# coding: utf-8
#
""" pyIBGE: A module to access data from the Brazilian Institute
 of Geography and Statistics (IBGE)
 (c) 2016 Renan Birck Pinheiro [renan.ee.ufsm@gmail.com]

 Module where the main query functions are defined.
 Presently, this is a very, VERY thin wrapper arround the API. """

from collections import OrderedDict
from lxml import html
import requests

class IBGEQuery:
    """ The class that represents a query.
    It receives the table ID and the parameters (available on the API documentation)."""

    class Entry:
        """ namedtuple doesn't suit us since it's immutable.
            then, this class is a simple struct-like implementation. """
        def __init__(self, name=None, value=None):
            self.name = name
            self.value = value

    def __init__(self, table_ID=None, params=None):
        self.has_help = False
        if 0 < table_ID < 9999:
            self.my_table_ID = table_ID
        else:
            raise ValueError("Table ID must be between 0 and 9999.")
        if not params:
            raise ValueError("Need to specify what params you want.")
        elif '/t/' in params:
            raise ValueError("Do not specify the 't' parameter in params, it is set by table_ID")
        else:
            self.params = params

    @property
    def table_ID(self):
        """ Just an alias for my_table_ID. """
        return self.my_table_ID

    # Those ensure that the 'has_help' variable is properly (re)set upon changing the table.
    @table_ID.setter
    def table_ID(self, table_ID):
        """ Resets the has_help variable upon changing the table ID. """
        self.has_help = False
        self.my_table_ID = table_ID

    @table_ID.getter
    def table_ID(self):
        """ Just an alias for my_table_ID. """
        return self.my_table_ID

    def build_URL(self):
        """ Builds the URL for the queery. """

        constant_part = "http://api.sidra.ibge.gov.br/values"
        variable_part = '/t/' + str(self.table_ID)

        if self.params[0] != '/':
            variable_part += '/'

        variable_part += self.params

        return constant_part + variable_part

    def get_table_info(self):
        """ Gets the information (table title, variables, periods...)
        of the table. """

        if self.has_help:
            # We've already been there. Spare us the network request.
            return

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
        except IndexError:
            unavailable_table = ""


        if 'Tabela não possui dados de uso público' in unavailable_table:
            raise ValueError("This table is not available to the public.")

        # Now walk the HTML.
        table_title = help_tree.xpath('//*[@id="lblNomeTabela"]/text()')[0]
        self.table_info['table_name'] = table_title

        table_survey = help_tree.xpath('//*[@id="lblNomePesquisa"]/text()')[0]
        self.table_info['table_survey'] = table_survey

        table_theme = help_tree.xpath('//*[@id="lblNomeAssunto"]/text()')[0]
        self.table_info['table_theme'] = table_theme

        self.has_help = True    # We got the help information. Don't redo the query
                                # unless the table changes.

    def get_data(self):
        """ Retrieves the data and then loads the result into the 'variables' object. """
        url = self.build_URL()
        data = requests.get(url).json(object_pairs_hook=OrderedDict)
        self.variables = {}
        header, content = data[0], data[1:]
        self.num_results = len(content)

        # Chew on the header and create a structure to hold the data we will parse next.
        for key in header.keys():
            self.variables[key] = self.Entry(name=header[key],
                                             value=[None] * self.num_results)

        # Chew on the contents, loading them a line at a time.
        # I wanted to do this as a list comprehension, but this is not a good idea.
        # cf. http://stackoverflow.com/questions/10291997/

        for (line_number, content_line) in enumerate(content):
            #print("Parsing line ", line_number)
            for key in content_line.keys():
            #    print(key, " -> ", content_line[key])

                # namedtuples are immutable, then we have todo this
                self.variables[key].value[line_number] = content_line[key]
