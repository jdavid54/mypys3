import csv
import pandas as pd

num_elements = 118

with open('/home/pi/Desktop/elements.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\'')
    for row in spamreader:
        print(', '.join(row))
        
data = pd.read_csv('elements.csv').reset_index()
data['index'] = 118-data['index'].astype('int32')
pd.to_numeric(data['Pointdefusion'])
pd.to_numeric(data['Pointébullition'])
data = data.sort_values('index').set_index('index')
print(data.info())
num = 6
print(data.loc[num])

data2 = pd.read_csv('elements_configelectronique.csv') #.reset_index()

elements = pd.merge(data, data2, how='left', on='Numéroatomique')
elements.info()

elements['Configurationelectronique'] = elements['Configurationelectronique'].replace(' ','-')

elem = 21
print(elements.loc[elem-1])
print(elements.loc[elem-1]['Configurationelectronique'])

print('Nom_x','Numéroatomique','Masseatomique','Configurationelectronique')
for el in range(1,num_elements):
    print(', '.join([str(e) for e in (elements.loc[el-1][['Nom_x','Numéroatomique','Masseatomique','Configurationelectronique']].values.tolist())]))