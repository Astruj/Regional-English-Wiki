#import csv
from matplotlib import pyplot as plt
import pandas as pd



df = pd.read_csv ('fr_data.csv')
data = list(df['Number Of Unique Editors'])
print(data)
fr_len = len(data)
print(fr_len)

df = pd.read_csv('en_data.csv')
data1 = list(df['numEditors'])
data.extend(data1)
tot_len = len(data)
print(data)
print(tot_len)

x = []
for i in range(1,tot_len+1):
    if(i<=fr_len):
        temp = 'fr'
        temp = temp + str(i)
    else:
        temp = 'en'
        temp = temp + str(i-fr_len)
    x.append(temp)     

print(x)


fig, ax= plt.subplots()
#for color in ['tab:blue', 'tab:orange', 'tab:green']:

ax.scatter(x[0:fr_len],data[0:fr_len], c='tab:green', label='french',alpha=1, edgecolors='none')
ax.scatter(x[fr_len:tot_len],data[fr_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('editors : COVID-19 pandemic in France')
plt.ylabel('numEditors')
plt.xlabel('articles')

#plt.show()
plt.savefig('editors.png')

##################
##########################

#pageviews

##########################
#################


df = pd.read_csv ('fr_data.csv')
data = list(df['Pageviews'])
print(data)
fr_len = len(data)
print(fr_len)

df = pd.read_csv('en_data.csv')
data1 = list(df['pageviews'])
data.extend(data1)
tot_len = len(data)
print(data)
print(tot_len)

x = []
for i in range(1,tot_len+1):
    if(i<=fr_len):
        temp = 'fr'
        temp = temp + str(i)
    else:
        temp = 'en'
        temp = temp + str(i-fr_len)
    x.append(temp)     

print(x)



fig, ax= plt.subplots()
#for color in ['tab:blue', 'tab:orange', 'tab:green']:

ax.scatter(x[0:fr_len],data[0:fr_len], c='tab:green', label='french',alpha=1, edgecolors='none')
ax.scatter(x[fr_len:tot_len],data[fr_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('Pageviews - COVID-19 pandemic in France')
plt.ylabel('pageviews')
plt.xlabel('articles')

#plt.show()
plt.savefig('pageviews.png')




####################
######################

#readability

##################
#########################

df = pd.read_csv ('fr_data.csv')
data = list(df['Readability'])
print(data)
fr_len = len(data)
print(fr_len)

df = pd.read_csv('en_data.csv')
data1 = list(df['readability'])
data.extend(data1)
tot_len = len(data)
print(data)
print(tot_len)

x = []
for i in range(1,tot_len+1):
    if(i<=fr_len):
        temp = 'fr'
        temp = temp + str(i)
    else:
        temp = 'en'
        temp = temp + str(i-fr_len)
    x.append(temp)     

print(x)



fig, ax= plt.subplots()
#for color in ['tab:blue', 'tab:orange', 'tab:green']:

ax.scatter(x[0:fr_len],data[0:fr_len], c='tab:green', label='french',alpha=1, edgecolors='none')
ax.scatter(x[fr_len:tot_len],data[fr_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('corresponding to COVID-19 pandemic in France')
plt.ylabel('readability')
plt.xlabel('articles')

#plt.show()
plt.savefig('readability.png')


#######################
#########################
#pageviews / editor
#########################
###########################


df = pd.read_csv ('fr_data.csv')
pageviews = list(df['Pageviews'])
numEditors = list(df['Number Of Unique Editors'])
ratio = []
for i in range(0,len(pageviews)):
    ratio.append(pageviews[i]/numEditors[i])
print(ratio)
fr_len = len(ratio)
print(fr_len)



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
    if(i<=fr_len):
        temp = 'fr'
        temp = temp + str(i)
    else:
        temp = 'en'
        temp = temp + str(i-fr_len)
    x.append(temp)     

print(x)


fig, ax= plt.subplots()
#for color in ['tab:blue', 'tab:orange', 'tab:green']:

ax.scatter(x[0:fr_len],ratio[0:fr_len], c='tab:green', label='french',alpha=1, edgecolors='none')
ax.scatter(x[fr_len:tot_len],ratio[fr_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('corresponding to COVID-19 pandemic in France')
plt.ylabel('pageviews / editor')
plt.xlabel('articles')

#plt.show()
plt.savefig('pgviewsPerEditor.png')



#################
###################
#revisions
##################
#####################

df = pd.read_csv ('fr_data.csv')
data = list(df['Revisions'])
print(data)
fr_len = len(data)
print(fr_len)

df = pd.read_csv('en_data.csv')
data1 = list(df['revisions'])
data.extend(data1)
tot_len = len(data)
print(data)
print(tot_len)

x = []
for i in range(1,tot_len+1):
    if(i<=fr_len):
        temp = 'fr'
        temp = temp + str(i)
    else:
        temp = 'en'
        temp = temp + str(i-fr_len)
    x.append(temp)     

print(x)


fig, ax= plt.subplots()
#for color in ['tab:blue', 'tab:orange', 'tab:green']:

ax.scatter(x[0:fr_len],data[0:fr_len], c='tab:green', label='french',alpha=1, edgecolors='none')
ax.scatter(x[fr_len:tot_len],data[fr_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('corresponding to COVID-19 pandemic in France')
plt.ylabel('revisions')
plt.xlabel('articles')

#plt.show()
plt.savefig('revisions.png')



###############
########################
#revison/editor
#######################
#############


df = pd.read_csv ('fr_data.csv')
revisions = list(df['Revisions'])
numEditors = list(df['Number Of Unique Editors'])
ratio = []
for i in range(0,len(revisions)):
    ratio.append(revisions[i]/numEditors[i])
print(ratio)
fr_len = len(ratio)
print(fr_len)



df = pd.read_csv('en_data.csv')
revisions = list(df['revisions'])
numEditors = list(df['numEditors'])
ratio1 = []
for i in range(0,len(revisions)):
    ratio1.append(revisions[i]/numEditors[i])

ratio.extend(ratio1)
tot_len = len(ratio)
print(ratio)
print(tot_len)


x = []
for i in range(1,tot_len+1):
    if(i<=fr_len):
        temp = 'fr'
        temp = temp + str(i)
    else:
        temp = 'en'
        temp = temp + str(i-fr_len)
    x.append(temp)     

print(x)


fig, ax= plt.subplots()
#for color in ['tab:blue', 'tab:orange', 'tab:green']:

ax.scatter(x[0:fr_len],ratio[0:fr_len], c='tab:green', label='hindi',alpha=1, edgecolors='none')
ax.scatter(x[fr_len:tot_len],ratio[fr_len:tot_len], c='tab:orange', label='english',alpha=1, edgecolors='none')


ax.legend()
ax.set_facecolor('lightpink')
#ax.grid(True)
plt.title('corresponding to COVID-19 pandemic in France')
plt.ylabel('revisions / editor')
plt.xlabel('articles')

#plt.show()
plt.savefig('revisionPerEditor.png')







