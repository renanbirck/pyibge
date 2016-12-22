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
