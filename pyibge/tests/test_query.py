#!/usr/bin/env python3
#
# pyIBGE: A module to access data from the Brazilian Institute of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]
#
# This module runs a few tests on the query. 

from unittest import TestCase
import pyibge 

class TestExtraRoutines(TestCase):
    def test_create_invalid_query(self):
        """ Test creating some invalid queries
            to see how we deal with them. """
        with self.assertRaises(ValueError):
            pyibge.IBGEQuery(table_ID=0)

        with self.assertRaises(TypeError):
            pyibge.IBGEQuery()  # Null table ID raises error!

        with self.assertRaises(ValueError): # Valid table ID but no parameters given
            pyibge.IBGEQuery(table_ID=2149, params=None)

        with self.assertRaises(ValueError): # Contradicting parameters (table_id vs /t/ in params string)
            pyibge.IBGEQuery(table_ID=2149, params='/t/2150')

    def test_build_url(self):
        """ Test building a simple query URL. The minimal query has
        the table ID (t) and the view (n or g elements)."""

        query = pyibge.IBGEQuery(table_ID=1612, params='n2')
        self.assertEqual(query.URL(), 'http://api.sidra.ibge.gov.br/values/t/1612/n2')

        query = pyibge.IBGEQuery(table_ID=2194, params='n3')
        self.assertEqual(query.URL(), 'http://api.sidra.ibge.gov.br/values/t/2194/n3')
        