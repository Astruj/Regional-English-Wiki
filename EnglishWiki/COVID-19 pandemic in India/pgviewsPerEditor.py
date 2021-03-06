#import csv
from matplotlib import pyplot as plt
import pandas as pd



df = pd.read_csv ('hi_data.csv')
pageviews = list(df['pageviews'])
numEditors = list(df['length_of_authors_list'])
ratio = []
for i in range(0,len(pageviews)):
    ratio.append(pageviews[i]/numEditors[i])
print(ratio)
hi_len = len(ratio)
print(hi_len)



df = pd.read_csv('en_data.csv')
pageviews = list(df['pageviews'])
numEditors = list(df['numEditors'])
ratio1 = []
for i in range(0,len(pageviews)):
    ratio1.append(pageviews[i]/numEditors[i])

ratio.extend(ratio1)
tot_len = len(ratio)
print(ratio)
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

ax.scatter(x[0:hi_len],ratio[0:hi_len], c='tab:green', label='hindi',alpha=1, edgecolors='none')
ax.scatter(x[hi_len:tot_len],ratio[hi_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('corresponding to COVID-19 pandemic in India')
plt.ylabel('pageviews / editor')
plt.xlabel('articles')

plt.show()

