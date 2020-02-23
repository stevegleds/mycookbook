import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import FuncFormatter
os.chdir('matplotlib/')  # to save plot files in the right folder


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
print('Starting to build plot first plot')
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

# Add average line
avg = top_10['Sales'].mean()
ax.axvline(x=avg, color='b', label='Average', linestyle='--', linewidth=2)
# Annotate new customers - random 3, 5, 8
for cust in [3, 5, 8]:
    ax.text(avg, cust, "New Customer")
print('Showing first plot')
# This version saves the plot as a png with opaque background.
# I have also specified the dpi and bbox_inches="tight" in order to minimize excess white space.
fig.savefig('sales-single.png', transparent=False, dpi=80, bbox_inches="tight")
plt.show()
print('Creating dual plot')
# Dual Plot
# Get the figure and axis
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(7, 4))

# Revenue plot
top_10.plot(kind='barh', y='Sales', x='Name', ax=ax0)
ax0.set_xlim([-10000, 140000])
ax0.set(title='Revenue', xlabel='Total Revenue', ylabel='Customers')
ax0.axvline(x=avg, color='b', label='Average', linestyle='--', linewidth=2)

# Unit sales plot
top_10.plot(kind='barh', y='Purchases', x='Name', ax=ax1)
avg = top_10['Purchases'].mean()
ax1.set(title='Units', xlabel='Total Units', ylabel='')
ax1.axvline(x=avg, color='b', label='Average', linestyle='--', linewidth=1)

# Title the figure
fig.suptitle('2014 Sales Analysis', fontsize=14, fontweight='bold')

# HIde the legends
ax0.legend().set_visible(False)
ax1.legend().set_visible(False)
print(f"printing second dual plot")
fig.savefig('sales-dual.png', transparent=False, dpi=80, bbox_inches="tight")
plt.show()

print('end')
