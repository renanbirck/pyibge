#!/usr/bin/env python3
#
# pyIBGE: A module to access data from the Brazilian Institute of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]
#
# This module runs a few tests on the extra routines. 

from unittest import TestCase
import pyibge

class TestExtraRoutines(TestCase):
    def test_convert_state_to_ID(self):
        """ Converts the state abbreviation to the state ID. """
        states = [('AC', 12), ('AL', 27), ('AP', 16),
                  ('AM', 13), ('BA', 29), ('CE', 23),
                  ('DF', 53), ('ES', 32), ('GO', 52),
                  ('MA', 21), ('MT', 51), ('MS', 50),
                  ('MG', 31), ('PA', 15), ('PB', 25),
                  ('PR', 41), ('PE', 26), ('PI', 22),
                  ('RJ', 33), ('RN', 24), ('RS', 43),
                  ('RO', 11), ('RR', 14), ('SC', 42),
                  ('SP', 35), ('SE', 28), ('TO', 17)]


        for (state, state_id) in states:
            print(state)
            self.assertEqual(state_id, pyibge.state_to_id(state))

        # Try to look an invalid state.
        with self.assertRaises(KeyError):
            pyibge.state_to_id('XY')