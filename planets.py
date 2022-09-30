import csv
# csv1
# with open('planets.txt', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='\'')
#     for row in spamreader:
#         print(', '.join(row))

import pandas as pd

data = pd.read_csv('planets.txt',)
df=data.T.reset_index()
df.columns=df.iloc[0]
df=df.drop(0).reset_index(drop=True) # no index
#df=pd.to_numeric(df) => error

def show_planet(num):    
    planet = df.loc[[num],df.columns[:]].T
    print(planet)

for i,c in enumerate(df.columns[1:]):
    print(c)
    if i not in (6,7,11,13,20):
        df[c]=pd.to_numeric(df[c])
    
df.info()

def save_csv(data):
    with open('planets.csv','w' ) as csvfile:
        #writer = csv.writer(csvfile)
        df.to_csv(csvfile, index=False)
    print('dataframe saved')

save_csv(df)

print('Demi-grand axe\n',df[df.columns[2:4]])

planet_num = 2
show_planet(planet_num)

