import hindi_wiki_module

# parse the dump
hindi_wiki_module.parse_dump(
    'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.xml')

# get number of revisions for an article
print(hindi_wiki_module.get_number_of_revisions('नागरिकता (संशोधन) अधिनियम, २०१९',
                                                'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'))

# get number of unique editors for an article
print(hindi_wiki_module.get_number_of_unique_editors('नागरिकता (संशोधन) अधिनियम, २०१९',
                                                     'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'))

# get total number of bytes edited for every revision of an article
print(hindi_wiki_module.get_number_of_bytes_edited('नागरिकता (संशोधन) अधिनियम, २०१९',
                                                   'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'))


# get list of all the articles present in a category
print(hindi_wiki_module.get_all_articles_in_a_category("वन्य जीवन"))


# get readability score of an article
print(hindi_wiki_module.get_readability_score(
    'नागरिकता (संशोधन) अधिनियम, २०१९'))

# get number of pageviews of an article
print(hindi_wiki_module.get_number_of_pageviews(
    'नागरिकता (संशोधन) अधिनियम, २०१९'))

article_list = ['नागरिकता संशोधन अधिनियम का विरोध',
                'नागरिकता (संशोधन) अधिनियम, २०१९',
                'शाहीन बाग विरोध प्रदर्शन',
                'भारतीय राष्ट्रीय नागरिक रजिस्टर',
                'राष्ट्रीय नागरिक रजिस्टर',
                'पीएम केयर्स फंड',
                'आरोग्य सेतु',
                'भारत में कोरोनावायरस से लॉकडाउन 2020',
                'भारत में कोरोनावायरस महामारी का आर्थिक प्रभाव',
                'भारत में 2020 कोरोनावायरस महामारी की समयरेखा',
                '2020 भारत में कोरोनावायरस महामारी',
                '2020 तमिल नाडु में कोरोनावायरस महामारी',
                '2020 उत्तर प्रदेश में कोरोनावायरस महामारी',
                '2020 महाराष्ट्र में कोरोनावायरस महामारी',
                '2020 पंजाब, भारत में कोरोनावायरस महामारी',
                'नोटा (भारत)',
                'राष्ट्रीय मतदाता दिवस',
                'परिसीमन आयोग'
                ]

gini_dict = hindi_wiki_module.gini_coefficient_of_article_list(article_list,
                                                               'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv')

filename = "hi_ginni.csv"
with open(filename, "w+", encoding="utf-8") as f:
    writer = csv.writer(f)
    for k, v in gini_dict.items():
        writer.writerow([k, v])
