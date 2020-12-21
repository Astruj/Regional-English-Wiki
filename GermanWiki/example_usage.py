import german_wiki_module
import csv
from googletrans import Translator
import pandas as pd


# parse the dump
german_wiki_module.parse_dump(
    'dewiki-20201020-stub-meta-history.xml/dewiki-20201020-stub-meta-history.xml')

# get number of revisions for an article
print(german_wiki_module.get_number_of_revisions('Luftstreitkräfte der Sowjetunion',
                                                 'dewiki-20201020-stub-meta-history.xml/dewiki-20201020-stub-meta-history.csv'))

# get number of unique editors for an article
print(german_wiki_module.get_number_of_unique_editors('Luftstreitkräfte der Sowjetunion',
                                                      'dewiki-20201020-stub-meta-history.xml/dewiki-20201020-stub-meta-history.csv'))

# get total number of bytes edited for every revision of an article
print(german_wiki_module.get_number_of_bytes_edited('Luftstreitkräfte der Sowjetunion',
                                                    'dewiki-20201020-stub-meta-history.xml/dewiki-20201020-stub-meta-history.csv'))


# get list of all the articles present in a category
print(german_wiki_module.get_all_articles_in_a_category(
    'Luftstreitkräfte der Sowjetunion'))


# get readability score of an article
print(german_wiki_module.get_readability_score(
    'Luftstreitkräfte der Sowjetunion'))

# get number of pageviews of an article
print(german_wiki_module.get_number_of_pageviews(
    'Luftstreitkräfte der Sowjetunion'))


# get list of  the all articles present in a category
category_list = ['COVID-19-Pandemie in Deutschland', 'Corona-Warn-App', 'Christian Drosten',
                 'COVID-19 Case-Cluster-Study', 'Alexander S. Kekulé',
                 'COVID-19-Pandemie in Deutschland/Statistik',
                 'Proteste gegen Schutzmaßnahmen wegen der COVID-19-Pandemie in Deutschland']
# print(category_list)


# save results to csv file
parameters = ['article', 'readability']
filename = "de_data.csv"
with open(filename, "w+", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(parameters)
    for x in category_list:
        article = x
        readability = german_wiki_module.get_readability_score(x)
        data = [article, readability]
        writer.writerow(data)
