#!/usr/bin/env python3

import matplotlib.pyplot as plt
try:
    import seaborn as sns
except:
    print("seaborn not found, your plots won't look as good")

import pyibge

# Table 915: number of informers, number of chickens and eggs produced
# p/201803: 3rd trimester of 2018
# v/29: number of eggs produced (thousand dozens)
# c12716/115236: trimester total
# n3/all: all states of Brazil

query = pyibge.IBGEQuery(table_ID=915, params='p/201802/v/29/c12716/115236/n3/all')
query.get_data()

values = []

for (state, value) in zip(query.variables['D4N'].value, query.variables['V'].value):
    try:
        values.append((state, int(value)))
    except:
        print("State of ", state, " has X in the value column. This means some data is censored.")

values.sort(key=lambda value: value[1])
print(values)

pos = range(len(values))

labels, amounts = zip(*values)

plt.barh(pos, amounts, align='center', log=True)
plt.yticks(pos, labels)
plt.xlabel('Ovos (milhares de dúzias)')
plt.tight_layout()
plt.show()
