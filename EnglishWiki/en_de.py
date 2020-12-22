import en_wiki_module
import os
import csv

current_dir = os.getcwd()

# cotegory name
category = 'COVID-19 pandemic in Germany'

current_dir = current_dir+'/'+category+'/'
os.mkdir(category)
os.chdir(current_dir)
current_dir = os.getcwd()
print(current_dir)


category_list = ['COVID-19 pandemic in Germany','Corona-Warn-App','Christian Drosten','COVID-19 Case-Cluster-Study','Alexander Kekulé','Statistics of the COVID-19 pandemic in Germany']

#download article dumps in knolml format
for category_members in category_list:
    input("Press any key to download new article dump:")
    print('\n')
    en_wiki_module.download_articles_of_cotegory(category_members,current_dir)
    print('\n')
    

#list of num revisions
numRev = en_wiki_module.get_number_of_revisions(current_dir)
print("Collecting data to csv...")
parameters = ['article','numEditors', 'pageiews','readability','revisions']
filename = "en_data.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    for i in category_list :
        print(i)
        data = [i,en_wiki_module.get_number_of_unique_editors(i,current_dir),en_wiki_module.get_number_of_pageviews(i), en_wiki_module.get_readability_score(i),numRev[i]]
        writer.writerow(data)

        
print(en_wiki_module.get_readability_score('Statistics of the COVID-19 pandemic in Germany'))

#editorlist
print("Collecting editor list to csv...")
parameters = ['Article','Editors']
filename = "en_editors.csv"
with open(filename, "w+") as f: 
    writer = csv.writer(f)
    writer.writerow(parameters)
    for i in category_list :
        editors = en_wiki_module.get_list_of_unique_editors(i,current_dir)
        x = [[el] for el in editors] 
        for each in x:
            data = [i,each[0]]
            writer.writerow(data)
  

print("FINISHED")




