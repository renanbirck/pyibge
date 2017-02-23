#!/usr/bin/env python3

# Example to get data from the PNAD (Pesquisa Nacional por Amostra de Domicílios) and
# plot the unemployment/underemployment levels.

import matplotlib.pyplot as plt
try:
    import seaborn as sns
except:
    print("seaborn not found, your plots won't look as good")

import pyibge

# Table ID: 4100 (Unemploment/underemployment)
# p/all: all the data available
# v/1641: people 14 or older, in thousands
# c604/40286: unemployed or in potential workforce (looking for job) or underemployed (<30 hours)
# n6/4205407: city/Florianópolis

query = pyibge.IBGEQuery(table_ID=4100, params='p/all/v/1641/c604/40286/n6/4205407')
query.get_data()

trimesters = [pyibge.period_to_date(x) for x in query.variables['D1C'].value]
values = [int(x) for x in query.variables['V'].value]

print("Trimesters is ", trimesters)
print("Values is ", values)


ticks = list(range(len(values))) # XXX: ugly hack
plt.ylim([min(values)-2, max(values)+2])

plt.plot(ticks, values, 'g-o')
plt.xticks(ticks, trimesters, fontsize=8, rotation=45)

plt.title('Subutilização da força de trabalho: Florianópolis', fontsize=16)
plt.xlabel("Trimestre")
plt.ylabel("População desocupada (milhares)")

try:
    sns.despine()
except(NameError):
    pass

plt.tight_layout()
plt.show()