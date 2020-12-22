#import csv
from matplotlib import pyplot as plt
import pandas as pd
import csv


df = pd.read_csv ('ru_data.csv')
ru_articles = list(df['article'])
pageviews1 = list(df['Pageviews'])
numArticles1 = len(ru_articles)
temp = 0
for i in range(0,numArticles1):
    temp = temp + pageviews1[i]
avg1 = temp/numArticles1

df = pd.read_csv ('en_data.csv')
en_articles = list(df['article'])
pageviews2 = list(df['pageviews'])
numArticles2 = len(en_articles)
temp = 0
for i in range(0,numArticles2):
    temp = temp + pageviews2[i]
avg2 = temp/numArticles2


parameters = ['Article','Average pageviews in a category']
filename = "averagePageviewsTable1.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    row = ['Russian', avg1]
    writer.writerow(row)
    row = []
    writer.writerow(row)
    writer.writerow(row)
    row = ['English', avg2]
    writer.writerow(row)   

################
###################
#pgviewsPerEditor
###################
##################


df = pd.read_csv ('ru_data.csv')
ru_articles = list(df['article'])
pageviews = list(df['Pageviews'])
numEditors = list(df['Number Of Unique Editors'])
ratio1 = []
for i in range(0,len(pageviews)):
    ratio1.append(pageviews[i]/numEditors[i])
print(ratio1)
ru_len = len(ratio1)
print(ru_len)


df = pd.read_csv('en_data.csv')
en_articles = list(df['article'])
pageviews = list(df['pageviews'])
numEditors = list(df['numEditors'])
ratio2 = []
for i in range(0,len(pageviews)):
    ratio2.append(pageviews[i]/numEditors[i])

en_len = len(ratio2)
print(ratio2)
print(en_len)

parameters = ['Article','Ratio pageviews/editors']
filename = "ru_pgviewsPerEditorTable1.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    x = 0
    for i in range(0,ru_len):
        row = [ru_articles[i],ratio1[i]]
        x = x +ratio1[i]
        writer.writerow(row)
    row = ['Average', x/ru_len]
    writer.writerow(row)

parameters = ['Article','Ratio pageviews/editors']
filename = "en_pgviewsPerEditorTable1.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    x = 0
    for i in range(0,en_len):
        row = [en_articles[i],ratio2[i]]
        x = x +ratio2[i]
        writer.writerow(row)
    row = ['Average', x/en_len]
    writer.writerow(row)


###############

#############


df = pd.read_csv ('ru_data.csv')
ru_articles = list(df['article'])
revisions1 = list(df['Revisions'])
numArticles1 = len(ru_articles)
temp = 0
for i in range(0,numArticles1):
    temp = temp + revisions1[i]
avg1 = temp/numArticles1

df = pd.read_csv ('en_data.csv')
en_articles = list(df['article'])
revisions2 = list(df['revisions'])
numArticles2 = len(en_articles)
temp = 0
for i in range(0,numArticles2):
    temp = temp + revisions2[i]
avg2 = temp/numArticles2




parameters = ['Article','Average revisions in a  category']
filename = "averageRevisionsTable1.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)

    row = ['Russian', avg1]
    writer.writerow(row)
    row = []
    writer.writerow(row)
    writer.writerow(row)


    row = ['English', avg2]
    writer.writerow(row)   


####
#revisionsPerEDITOR
#########

df = pd.read_csv ('ru_data.csv')
ru_articles = list(df['article'])
revisions = list(df['Revisions'])
numEditors = list(df['Number Of Unique Editors'])
ratio1 = []
for i in range(0,len(revisions)):
    ratio1.append(revisions[i]/numEditors[i])
print(ratio1)
ru_len = len(ratio1)
print(ru_len)


df = pd.read_csv('en_data.csv')
en_articles = list(df['article'])
revisions = list(df['revisions'])
numEditors = list(df['numEditors'])
ratio2 = []
for i in range(0,len(revisions)):
    ratio2.append(revisions[i]/numEditors[i])

en_len = len(ratio2)
print(ratio2)
print(en_len)




parameters = ['Article','Ratio revisions/editors']
filename = "ru_revisionsPerEditorTable1.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    x = 0
    for i in range(0,ru_len):
        row = [ru_articles[i],ratio1[i]]
        x = x +ratio1[i]
        writer.writerow(row)
    row = ['Average', x/ru_len]
    writer.writerow(row)

parameters = ['Article','Ratio revisions/editors']
filename = "en_revisionsPerEditorTable1.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    x = 0
    for i in range(0,en_len):
        row = [en_articles[i],ratio2[i]]
        x = x +ratio2[i]
        writer.writerow(row)
    row = ['Average', x/en_len]
    writer.writerow(row)

    ##########