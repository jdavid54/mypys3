import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# colors
colors = mcolors.CSS4_COLORS  # type dict
print(colors['whitesmoke'])
print(colors.keys())

def ss(s):
    #subscript, supscript
    example_string = "A0B1C2D3E4F5G6H7I8J9"
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    print(example_string.translate(SUP))
    print(example_string.translate(SUB))
    #print('100 m'+'3'.translate(SUP))
    return s.translate(SUP)

# supscript
m3 = ss(' m3')
print('100'+ m3)

df = pd.read_csv('Consommation_eau.csv',)

df['Date'] = pd.to_datetime(df['Date'], utc=True)
df['Date'] = df['Date'].dt.tz_convert('Europe/Paris')
#df.info()

##### if csv contains values with separator comma in decimals
#df['Relevé mensuel'] = df.loc[:,'Relevé mensuel'].apply(lambda x: x.replace(',','.'))
#df.loc[:,'Conso/mois'] = df.loc[df['Conso/mois'].isna()==False,'Conso/mois'].apply(lambda x:  x.replace(',','.'))
#df.loc[:,'Conso/jour'] = df.loc[df['Conso/jour'].isna()==False,'Conso/jour'].apply(lambda x:  x.replace(',','.'))
# df['Relevé mensuel']=pd.to_numeric(df['Relevé mensuel'])
# df['Conso/mois']=pd.to_numeric(df['Conso/mois'])
# df['Conso/jour']=pd.to_numeric(df['Conso/jour'])

df.info()
print(df.tail(5))
print(df.describe())

print(df.max(numeric_only=True))
print(df.std())

# plotting
lightgrey = [0.95,0.95,0.95]
whitesmoke = [0.98,0.98,0.98]
plt.rcParams['axes.facecolor'] = colors['aqua'] #'#F5F5F5'

fig, ax= plt.subplots()
df['Conso/mois'].plot(kind='bar')
plt.title('Conso/mois')
plt.grid()
plt.ylabel('Volume consommé en'+ m3)
ax.set_axisbelow(True)
#plt.show()
fig, ax= plt.subplots()
df['Conso/mois'].plot(kind='hist')
plt.grid()
plt.show()

plt.rcParams['axes.facecolor'] = whitesmoke
fig, ax= plt.subplots()
df['Conso/jour'].plot(kind='bar')
plt.title('Conso/jour')
ax.set_axisbelow(True)
plt.ylabel('Volume consommé en'+m3)
plt.grid()
#plt.show()
fig, ax= plt.subplots()
df['Conso/jour'].plot(kind='hist')
plt.show()

df.hist(['Conso/mois','Conso/jour'],bins=10, xrot=45)
plt.show()

fig, ax= plt.subplots();df.boxplot(['Conso/mois'])
fig, ax= plt.subplots();df.boxplot(['Conso/jour'])
plt.show()