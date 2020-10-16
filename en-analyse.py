import readability
from langdetect import detect
import textstat
import kdap
import csv
from matplotlib import pyplot as plt
from matplotlib import style
from numpy import genfromtxt


k = kdap.analysis.knol()

#GINI
print( "Gini Coefficient :", k.get_global_gini_coefficient(dir_path = '/home/akash/Desktop/pro/output'))

#Pageviews
pageViews =k.get_pageviews(site_name = 'wikipedia',granularity= 'monthly',start = '2019-01-01',end ='2020-10-01',article_name = 'Citizenship (Amendment) Act, 2019')
#print(PageViews)
with open('/home/akash/Desktop/pro/pgviews.csv', 'w') as f:
    for key in pageViews.keys():
        f.write("%s,%s\n"%(key,pageViews[key]))

#REVISION_WISE
frames = k.frame(dir_path = '/home/akash/Desktop/pro/output')
frames = list(frames)

#Titles
title = '' + frames[0].get_title()
print("\n\t\tTitle of the article :",title,'\n')

#Number_Of_Editors
editors = k.get_editors(dir_path = '/home/akash/Desktop/pro/output')
print("Number Of Unique Editors for article -",title," :",len(set(editors[title])),'\n')

lst = list(set(editors[title]))
print(lst[0])
x = [[el] for el in lst] 

file = open('/home/akash/Desktop/pro/en_editors.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    for each in x:
          write.writerow(each)

n = len(frames)

#Num_Of_Revisions
print("Total revisions :", n)

parameters = ['Rev', 'Bytes', 'Readability']
filename = "rev_data.csv"
with open(filename, 'a') as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)

    for i in range(0,n,5):

        print("Revision No. :", i)

        #Num_Of_Bytes
        Bytes = frames[i].get_bytes()
        print("Length in Bytes :",Bytes)

        #Get_Text_Of_This_Rev
        text = frames[i].get_text(clean=True)
        text = ''+text['text']

        #Language
        language = detect(text)
        print("Language :", language)

        #Readability_Using_Textstat_lib
        rd1 = textstat.flesch_reading_ease(text)
        print("Readability 1 :",rd1)

        #Readability_Using_Readability_lib
        d = readability.getmeasures(text,lang = language)
        rd2 = d['readability grades']['FleschReadingEase']
        print("Readability 2:",rd2)

        #Average_Readbility
        av = (rd1+rd2)/2
        print("Average Readability :", av )
        print('\n\n')

        data = [i,Bytes,av]


##plot
# data = genfromtxt('rev_data.csv', delimiter=',', names=['x', 'y','z'])
# plt.plot(data['x'], data['z'])

# plt.title('Readability - Revisions')
# plt.ylabel('Readability')
# plt.xlabel('Revisions')

# plt.plot()
# plt.show()

# wikiapi for list

# wiki_wiki = wikipediaapi.Wikipedia('en')
# def print_categorymembers(categorymembers, level=0, max_level=1):
#         for c in categorymembers.values():
#             print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
#             if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
#                 print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)

# cat = wiki_wiki.page("Category:Citizenship Amendment Act protests")
# l = list(cat.categorymembers)
# print_categorymembers(l[0])