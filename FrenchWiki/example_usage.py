import french_wiki_module
import csv
from googletrans import Translator
import pandas as pd


# parse the dump
french_wiki_module.parse_dump(
    'frwiki-20191120-stub-meta-history.xml/frwiki-20191120-stub-meta-history.xml')

# get number of revisions for an article
print(french_wiki_module.get_number_of_revisions('Marche verte',
                                                 'frwiki-20191120-stub-meta-history.xml/frwiki-20191120-stub-meta-history.csv'))

# get number of unique editors for an article
print(french_wiki_module.get_number_of_unique_editors('Marche verte',
                                                      'frwiki-20191120-stub-meta-history.xml/frwiki-20191120-stub-meta-history.csv'))

# get total number of bytes edited for every revision of an article
print(french_wiki_module.get_number_of_bytes_edited('Marche verte',
                                                    'frwiki-20191120-stub-meta-history.xml/frwiki-20191120-stub-meta-history.csv'))


# get list of all the articles present in a category
print(french_wiki_module.get_all_articles_in_a_category(
    'Marche verte'))


# get readability score of an article
print(french_wiki_module.get_readability_score(
    'Marche verte'))

# get number of pageviews of an article
print(french_wiki_module.get_number_of_pageviews(
    'Marche verte'))


# get list of  the all articles present in a category
category_list = ['Pandémie de Covid-19 en France', 'Église Porte ouverte chrétienne',
                 "Y a-t-il une erreur qu'ils n'ont pas commise ?"]


# save results to csv file
parameters = ['article', 'readability']
filename = "fr_data.csv"
with open(filename, "w+", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(parameters)
    for x in category_list:
        article = x
        readability = french_wiki_module.get_readability_score(x)
        data = [article, readability]
        writer.writerow(data)

article_list = ["Pandémie de Covid-19 en France",
                "Église Porte ouverte chrétienne",
                "Y a-t-il une erreur qu'ils n'ont pas commise ?",
                "Élections municipales de 2020 à Paris",
                "Élections sénatoriales françaises de 2020",
                "Élections municipales françaises de 2020"
                ]

gini_dict = french_wiki_module.gini_coefficient_of_article_list(article_list,
                                                                'frwiki-20191120-stub-meta-history.xml/frwiki-20191120-stub-meta-history.csv')

filename = "fr_ginni.csv"
with open(filename, "w+", encoding="utf-8") as f:
    writer = csv.writer(f)
    for k, v in gini_dict.items():
        writer.writerow([k, v])
