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
        states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        state_IDs = [12, 27, 16, 13, 29, 23, 53, 32, 52, 21, 50, 31, 15, 25, 41, 26, 22, 33, 24, 43, 11, 14, 42, 35, 28, 17]

        for (state, state_id) in zip(states, state_IDs):
            self.assertEquals(state_id, pyibge.state_to_id(state))
            
