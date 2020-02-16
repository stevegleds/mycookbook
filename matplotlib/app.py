import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def currency(x, pos):
    'x is the value and pos is position'
    if x >= 1000000:
        return '£{:1.1f}M'.format(x * 1e-6)  # not sure what all this does
    return '£{:1.0f}K'.format(x * 1e-3)


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
# Single Plot
fig, ax = plt.subplots(figsize=(14, 6))
# Subplot allows any future customization will be done via the ax or fig objects.
top_10.plot(kind='barh', y='Sales', x='Name', ax=ax)
ax.set_xlim([40000, 140000])
ax.set(title='2014 Revenue', xlabel='Total Revenue', ylabel='Customer')
formatter = FuncFormatter(currency)
ax.xaxis.set_major_formatter(formatter)
ax.legend().set_visible(False)
# Annotate new customers - random 3, 5, 8
for cust in [3, 5, 8]:
    ax.text(115000, cust, "New Customer")
# Add average line
avg = top_10['Sales'].mean()
ax.axvline(x=avg, color='b', label='Average', linestyle='--', linewidth=2)
plt.show()
# Dual Plot

print('end')
