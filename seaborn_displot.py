import pandas as pd
import csv
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

# https://seaborn.pydata.org/generated/seaborn.displot.html

penguins = sns.load_dataset("penguins")
sns.displot(data=penguins, x="flipper_length_mm")
plt.show()


sns.displot(data=penguins, x="flipper_length_mm", kind="kde")
plt.title('kind : kde')
plt.show()


sns.displot(data=penguins, x="flipper_length_mm", kind="ecdf")
plt.title('kind : edcf')
plt.show()

# distplot
sns.displot(data=penguins, x="flipper_length_mm", kde=True)
plt.title('kde : True')
plt.show()

sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm")
plt.show()

sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm", kind="kde")
plt.show()

g = sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm", kind="kde", rug=True)
plt.title('kind="kde", rug=True')
plt.show()

sns.displot(data=penguins, x="flipper_length_mm", hue="species", kind="kde")
plt.title('hue="species", kind="kde"')
plt.show()

sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.title('hue="species", multiple="stack"')
plt.show()

sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="sex", kind="kde")
plt.title('hue="species", col="sex", kind="kde"')
plt.show()

sns.displot(
    data=penguins, y="flipper_length_mm", hue="sex", col="species",
    kind="ecdf", height=4, aspect=.7,
)
plt.title('hue="sex", col="species", kind="ecdf"')
plt.show()


g = sns.displot(
    data=penguins, y="flipper_length_mm", hue="sex", col="species",
    kind="kde", height=4, aspect=.7,
)
g.set_axis_labels("Density (a.u.)", "Flipper length (mm)")
g.set_titles("{col_name} penguins")
plt.show()

