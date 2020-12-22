#import csv
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv ('hi_data.csv')
data = list(df['readability'])
print(data)
hi_len = len(data)
print(hi_len)

df = pd.read_csv('en_data.csv')
data1 = list(df['readability'])
data.extend(data1)
tot_len = len(data)
print(data)
print(tot_len)

x = []
for i in range(1,tot_len+1):
    if(i<=hi_len):
        temp = 'h'
        temp = temp + str(i)
    else:
        temp = 'en'
        temp = temp + str(i-hi_len)
    x.append(temp)     

print(x)



fig, ax= plt.subplots()
#for color in ['tab:blue', 'tab:orange', 'tab:green']:

ax.scatter(x[0:hi_len],data[0:hi_len], c='tab:green', label='hindi',alpha=1, edgecolors='none')
ax.scatter(x[hi_len:tot_len],data[hi_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('corresponding to COVID-19 pandemic in India')
plt.ylabel('readability')
plt.xlabel('articles')

plt.show()


# plt.scatter(x,data)

# plt.title('articles - pageviews')
# plt.ylabel('pageviews')
# plt.xlabel('articles')

# plt.plot()
# plt.show()
