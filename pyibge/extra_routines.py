#!/usr/bin/env python3
#
# pyIBGE: A module to access data from the Brazilian Institute of Geography and Statistics (IBGE)
# (c) 2016 Renan Birck Pinheiro [renan.birck.pinheiro@gmail.com]

# This module provides extra routines that can be useful while building a query. 

def state_to_id(state):
    """Convert a state to its ID as used by the IBGE databases. 
    Raises KeyError if the state is invalid. """
    
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

def period_to_date(period):
    """ Convert a period (in AAAAMM form) to a date (in MM/AAAA form). """
    month = period[4:6]
    year = period[0:4]

    return month + '/' + year

# Some constants:

ABS_ZERO = '-'       # Zero from nonexisting data 
COMPUTED_ZERO = '0'  # Zero from rounding
CENSORED = 'X'       # Zero from censored data
NA = '..'            # Zero from N/A data
ND = '...'           # Zero from unavailable data (e.g. city didn't exist)
