#import csv
from matplotlib import pyplot as plt
import pandas as pd
import csv


df = pd.read_csv ('hi_data.csv')
hi_articles = list(df['article'])
revisions = list(df['revisions'])
numEditors = list(df['length_of_authors_list'])
ratio1 = []
for i in range(0,len(revisions)):
    ratio1.append(revisions[i]/numEditors[i])
print(ratio1)
hi_len = len(ratio1)
print(hi_len)


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
filename = "hi_revisionsPerEditorTable2.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    x = 0
    for i in range(0,hi_len):
        row = [hi_articles[i],ratio1[i]]
        x = x +ratio1[i]
        writer.writerow(row)
    row = ['Average', x/hi_len]
    writer.writerow(row)

parameters = ['Article','Ratio revisions/editors']
filename = "en_revisionsPerEditorTable2.csv"
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