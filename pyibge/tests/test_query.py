#!/usr/bin/env python3
# coding: utf-8
#
# pyIBGE: A module to access data from the Brazilian Institute of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]
#
# This module runs a few tests on the query.

from unittest import TestCase
import pyibge

class TestQuery(TestCase):
    """ Test cases for the query module. """
    def test_create_invalid_query(self):
        """ Test creating some invalid queries
            to see how we deal with them. """
        with self.assertRaises(ValueError):
            pyibge.IBGEQuery(table_ID=0)

        with self.assertRaises(TypeError):
            pyibge.IBGEQuery()  # Null table ID raises error!

        with self.assertRaises(ValueError): # Valid table ID but no parameters given
            pyibge.IBGEQuery(table_ID=2149, params=None)

        with self.assertRaises(ValueError): # Contradicting parameters
                                            # (table_id vs /t/ in params string)
            pyibge.IBGEQuery(table_ID=2149, params='/t/2150')

    def test_build_url(self):
        """ Test building a simple query URL. The minimal query has
        the table ID (t) and the view (n or g elements)."""

        query = pyibge.IBGEQuery(table_ID=1612, params='n2')
        self.assertEqual(query.build_URL(), 'http://api.sidra.ibge.gov.br/values/t/1612/n2')

        query = pyibge.IBGEQuery(table_ID=2194, params='n3')
        self.assertEqual(query.build_URL(), 'http://api.sidra.ibge.gov.br/values/t/2194/n3')

    def test_get_table_info(self):
        """ Test trying to get table information and parsing it. """
        query = pyibge.IBGEQuery(table_ID=1000, params='n2')
        query.get_table_info()

        self.assertEqual(query.table_info['table_name'], 
        "Área plantada, área colhida, quantidade produzida e rendimento " \
        "médio de amendoim, 1ª e 2ª safras")

        self.assertEqual(query.table_info['table_survey'],
        "Produção Agrícola Municipal")

        self.assertEqual(query.table_info['table_theme'],
        "Lavouras temporárias")

        
    def test_unavailable_table_info(self):
        """ Test trying an unavailable table. """
        query = pyibge.IBGEQuery(table_ID=115, params='n2')
        with self.assertRaises(ValueError):
            query.get_table_info()

    def test_refresh_table(self):
        """ Test changing the table ID; has_help should change. """
        query = pyibge.IBGEQuery(table_ID=1000, params='n2')
        query.get_table_info()
        self.assertEqual(query.has_help, True)
        query.table_ID = 999
        self.assertEqual(query.has_help, False)

    def test_get_data(self):
        """ Run a query, and then check whether we receive the dictionaries. """

        query = pyibge.IBGEQuery(table_ID=4100, params='p/201201/v/1641/c604/31750/n6/4205407')
        query.get_data()

        # Check if the information was successfully read and parsed
        # from the JSON answer the server gave.

        self.assertEqual(query.variables['D1C'].name, 'Trimestre (Código)')
        self.assertEqual(query.variables['D1N'].name, 'Trimestre')

        self.assertEqual(query.variables['D2C'].name, 'Variável (Código)')
        self.assertEqual(query.variables['D2N'].name, 'Variável')

        self.assertEqual(query.variables['D3C'].name[0:4], 'Tipo')
        self.assertEqual(query.variables['D3N'].name[0:4], 'Tipo')
        
        self.assertEqual(query.variables['D4C'].name, 'Município (Código)')
        self.assertEqual(query.variables['D4N'].name, 'Município')

        self.assertEqual(query.variables['MC'].name, 'Unidade de Medida (Código)')
        self.assertEqual(query.variables['MN'].name, 'Unidade de Medida')

        self.assertEqual(query.variables['V'].name, 'Valor')
        
        # Check the received values
        self.assertEqual(query.variables['D1C'].value[0], '201201')
        self.assertEqual(query.variables['D1N'].value[0], '1º trimestre 2012')
        
        self.assertEqual(query.variables['D2C'].value[0], '1641')
        self.assertEqual(query.variables['D2N'].value[0], 'Pessoas de 14 anos ou mais de idade')

        self.assertEqual(query.variables['D3C'].value[0], '31750')
        self.assertEqual(query.variables['D3N'].value[0], 'Desocupado')

        self.assertEqual(query.variables['D4C'].value[0], '4205407')
        self.assertEqual(query.variables['D4N'].value[0], 'Florianópolis - SC')

        self.assertEqual(query.variables['MC'].value[0], '1572')
        self.assertEqual(query.variables['MN'].value[0], 'Mil pessoas')

        self.assertEqual(query.variables['V'].value[0], '9')

    def test_get_data_with_multiple_variables(self):
        query = pyibge.IBGEQuery(table_ID=4100, params='p/201201,201202/v/1641/c604/31750/n6/4205407')
        query.get_data()

        self.assertEqual(query.num_results, 2)
        
