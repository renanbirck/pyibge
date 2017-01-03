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

        self.assertEqual(query.table_info['table_name'], 'Área plantada, área colhida, quantidade produzida e rendimento médio de amendoim, 1ª e 2ª safras')
        
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