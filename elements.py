import csv
import pandas as pd

num_elements = 118

# csv1
with open('elements.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\'')
    for row in spamreader:
        print(', '.join(row))

# la liste est à l'envers : 118 à 1
data = pd.read_csv('elements.csv').reset_index()
data['index'] = 118-data['index'].astype('int32')
pd.to_numeric(data['Pointdefusion'])
pd.to_numeric(data['Pointébullition'])
data = data.sort_values('index').set_index('index')
print('\ndata info\n')
data.info() # pas besoin de print

num = 6
print('\ndata element 6\n',data.loc[num],'\n')

# csv2
data2 = pd.read_csv('elements_configelectronique.csv') #.reset_index()

elements = pd.merge(data, data2, how='left', on='Numéroatomique')
elements.info()

#elements['Configurationelectronique'] = elements['Configurationelectronique'].replace(' ','-')

elem = 21
print('\nelement 21\n',elements.loc[elem-1])
#print(elements.loc[elem-1]['Configurationelectronique'])

print('\nNom_x','Numéroatomique','Masseatomique','Configurationelectronique')
for e in range(1,num_elements+1):
    print(', '.join([str(e) for e in (elements.loc[e-1][['Nom_x','Numéroatomique','Masseatomique','Configurationelectronique']].values.tolist())]))