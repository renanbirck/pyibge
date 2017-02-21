#!/usr/bin/env python3

# Example to get data from the PNAD (Pesquisa Nacional por Amostra de Domicílios) and
# plot the unemployment/underemployment levels.

import matplotlib.pyplot as plt
try:
    import seaborn as sns
except:
    print("seaborn not found, your plots won't look as good")

import pyibge

query = pyibge.IBGEQuery(table_ID=4100, params='p/all/v/1641/c604/31750/n6/4205407')
query.get_data()

print(query.variables['D1C'].value)
