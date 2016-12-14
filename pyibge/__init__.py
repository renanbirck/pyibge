#!/usr/bin/env python3
#
# pyIBGE: A module to access data from the Brazilian Institute of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]


def test():
    return("hello world from pyibge")

def state_to_id(state):
    """Convert a state to its ID as used by the IBGE databases. """
    
    state = state.upper()

    states = {'AC': 12, 'AL': 27,
              'AP': 16, 'AM': 13,
              'BA': 29, 'CE': 23,
              'DF': 53, 'ES': 32,
              'GO': 52, 'MA': 21,
              'MT': 51, 'MS': 50,
              'MG': 31, 'PA': 15,
              'PB': 25, 'PR': 41,
              'PE': 26, 'PI': 22,
              'RJ': 33, 'RN': 24,
              'RS': 43, 'RO': 11,
              'RR': 14, 'SC': 42,
              'SP': 35, 'SE': 28,
              'TO': 17}

    return states[state]
