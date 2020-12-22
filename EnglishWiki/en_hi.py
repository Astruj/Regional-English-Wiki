import en_wiki_module
import os
import csv

current_dir = os.getcwd()

#category = 'Citizenship Amendment Act protests'

category = 'COVID-19 pandemic in India'

current_dir = current_dir+'/'+category+'/'
os.mkdir(category)
os.chdir(current_dir)
current_dir = os.getcwd()
print(current_dir)


category_list = ['PM CARES Fund','Aarogya Setu','COVID-19 pandemic lockdown in India','Economic impact of the COVID-19 pandemic in India','Timeline of the COVID-19 pandemic in India (January–May 2020)','Timeline of the COVID-19 pandemic in India (June–December 2020)','COVID-19 pandemic in Tamil Nadu','COVID-19 pandemic in Uttar Pradesh','COVID-19 pandemic in Maharashtra','COVID-19 pandemic in Punjab, India']

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




