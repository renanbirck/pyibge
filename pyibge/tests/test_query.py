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

    def test_build_url(self):
        """ Test building a simple query URL. The minimal query has
        the table ID (t) and the view (n or g elements)."""

        query = pyibge.IBGEQuery(table_ID=1612, level='n2')
        self.assertEqual(query.URL(), '/t/1612/n2')
        
        