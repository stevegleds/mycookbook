import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_excel(
    "https://github.com/chris1610/pbpython/blob/master/data/sample-salesv3.xlsx?raw=true"
)
print(df.head())
top_10 = (df.groupby('name')['ext price', 'quantity'].agg({
    'ext price': 'sum',
    'quantity': 'count'
}).sort_values(by='ext price', ascending=False))[:10].reset_index()

top_10.rename(columns={
    'name': 'Name',
    'ext price': 'Sales',
    'quantity': 'Purchases'
},
              inplace=True)

print(top_10)
print('Hi again')
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(
    5, 6))  # Any future customization will be done via the ax or fig objects.
top_10.plot(kind='barh', y='Sales', x='Name', ax=ax)
ax.set_xlim([10000, 140000])
ax.set_xlabel('Total Revenue')
ax.set_ylabel('Customer')
ax.legend().set_visible(False)
plt.show()
print('end')
