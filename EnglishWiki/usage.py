import en_wiki_module
import os
import csv

current_dir = os.getcwd()

#get the cotegory name
category = input('Please enter the title of article cotegory :')

# category = 'COVID-19 pandemic in France'

current_dir = current_dir+'/'+category+'/'
os.mkdir(category)
os.chdir(current_dir)
current_dir = os.getcwd()
print(current_dir)


# get list of all the articles present in a category
category_list = en_wiki_module.get_all_articles_in_a_category(category)
print(category_list)

#category_list = ['COVID-19 pandemic in France','Christian Open Door Church','Y a-t-il une erreur qu\'ILS n\'ont pas commise?']

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
        data = [i,en_wiki_module.get_number_of_unique_editors(i,current_dir),'g', en_wiki_module.get_readability_score(i),numRev[i]]
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




