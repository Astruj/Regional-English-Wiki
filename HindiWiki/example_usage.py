import hindi_wiki_module

# # parse the dump
# hindi_wiki_module.parse_dump(
#     'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.xml')

# # get number of revisions for an article
# print(hindi_wiki_module.get_number_of_revisions('नागरिकता (संशोधन) अधिनियम, २०१९',
#                                                 'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'))

# # get number of unique editors for an article
# print(hindi_wiki_module.get_number_of_unique_editors('नागरिकता (संशोधन) अधिनियम, २०१९',
#                                                      'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'))

# # get total number of bytes edited for every revision of an article
# print(hindi_wiki_module.get_number_of_bytes_edited('नागरिकता (संशोधन) अधिनियम, २०१९',
#                                                    'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'))


# # get list of all the articles present in a category
# print(hindi_wiki_module.get_all_articles_in_a_category("वन्य जीवन"))


# # get readability score of an article
print(hindi_wiki_module.get_readability_score(
    'नागरिकता (संशोधन) अधिनियम, २०१९'))

# # get number of pageviews of an article
# print(hindi_wiki_module.get_number_of_pageviews(
#     'नागरिकता (संशोधन) अधिनियम, २०१९'))
