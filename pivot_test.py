import pandas as pd

def test_pivot():
    data = pd.DataFrame({'country':['france','espagne','suisse','france','espagne','suisse'], 'religion':['cath','boud','prot','prot','prot','boud'], 'population':[10,11,12,40,45,25]})
    print(data)
    data = data.pivot(index='country', columns='religion', values='population')
    print(data)

test_pivot()