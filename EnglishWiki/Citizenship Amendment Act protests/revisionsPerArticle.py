#import csv
from matplotlib import pyplot as plt
import pandas as pd
import csv


df = pd.read_csv ('hi_data.csv')
hi_articles = list(df['article'])
revisions1 = list(df['revisions'])
numArticles1 = len(hi_articles)
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
filename = "averageRevisionsTable2.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)

    row = ['Hindi', avg1]
    writer.writerow(row)
    row = []
    writer.writerow(row)
    writer.writerow(row)


    row = ['English', avg2]
    writer.writerow(row)   
