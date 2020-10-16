# import wiki_dump_parser as parser
# parser.xml_to_csv(
#     'enwiki-20201001-pages-articles-multistream.xml/enwiki-20201001-pages-articles-multistream.xml')


import pandas as pd

chunksize = 10 ** 6
authors = []
bytes_list = []
filepath = 'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'
for chunk in pd.read_csv(filepath, quotechar='|', index_col=False, chunksize=chunksize):
    # chunk = chunk[chunk['page_title'] == '|मुख्य पृष्ठ|']
    # chunk = chunk[chunk['page_title'] == 'नागरिकता (संशोधन) अधिनियम, २०१९']
    chunk = chunk[chunk['page_title'] == 'भारत']
    # chunk = chunk[chunk['contributor_id'] == '1634']
    if not chunk.empty:
        authors.extend(list(chunk['contributor_id']))
        bytes_list = list(chunk['bytes'])
        print(chunk)

unique_authors = set(authors)
# print(authors, len(authors), type(authors))
# print(unique_authors)
print('number of unique authors : ',len(unique_authors))
count = 0
# print(bytes_list)
for x in bytes_list:
    count += x

print('total number of bytes',count)
