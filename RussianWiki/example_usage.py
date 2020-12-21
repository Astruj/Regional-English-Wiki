import russian_wiki_module
import csv
from googletrans import Translator
import pandas as pd


# parse the dump
russian_wiki_module.parse_dump(
    'ruwiki-20201020-stub-meta-history.xml/ruwiki-20201020-stub-meta-history.xml')

# get number of revisions for an article
print(russian_wiki_module.get_number_of_revisions('Министерство внутренних дел Российской Федерации',
                                                  'ruwiki-20201020-stub-meta-history.xml/ruwiki-20201020-stub-meta-history.csv'))

# get number of unique editors for an article
print(russian_wiki_module.get_number_of_unique_editors('Министерство внутренних дел Российской Федерации',
                                                       'ruwiki-20201020-stub-meta-history.xml/ruwiki-20201020-stub-meta-history.csv'))

# get total number of bytes edited for every revision of an article
print(russian_wiki_module.get_number_of_bytes_edited('Министерство внутренних дел Российской Федерации',
                                                     'ruwiki-20201020-stub-meta-history.xml/ruwiki-20201020-stub-meta-history.csv'))


# get list of all the articles present in a category
print(russian_wiki_module.get_all_articles_in_a_category(
    'Министерство внутренних дел Российской Федерации'))


# get readability score of an article
print(russian_wiki_module.get_readability_score(
    'Министерство внутренних дел Российской Федерации'))

# get number of pageviews of an article
print(russian_wiki_module.get_number_of_pageviews(
    'Министерство внутренних дел Российской Федерации'))


# get list of  the all articles present in a category
category_list = ['Распространение COVID-19 в России', 'Хронология распространения COVID-19 в России',
                 'Гам-КОВИД-Вак', 'Распространение COVID-19 в Крыму']
# print(category_list)


# save results to csv file
parameters = ['article', 'readability']
filename = "ru_data.csv"
with open(filename, "w+", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(parameters)
    for x in category_list:
        article = x
        readability = russian_wiki_module.get_readability_score(x)
        data = [article, readability]
        writer.writerow(data)
