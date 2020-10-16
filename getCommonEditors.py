import pandas as pd

chunksize = 10 ** 6
authors_hi = []
filepath = 'hiwiki-20201001-pages-meta-history.xml/hiwiki-20201001-pages-meta-history.csv'
for chunk in pd.read_csv(filepath, quotechar='|', index_col=False, chunksize=chunksize):
    # chunk = chunk[chunk['page_title'] == '|मुख्य पृष्ठ|']
    chunk = chunk[chunk['page_title'] == 'नागरिकता (संशोधन) अधिनियम, २०१९']
    # chunk = chunk[chunk['page_title'] == 'भारत']
    # chunk = chunk[chunk['contributor_id'] == '1634']
    if not chunk.empty:
        authors_hi.extend(list(chunk['contributor_id']))
        # print(chunk)

authors_hi = list(set(authors_hi))
authors_en = []
df = pd.read_csv('en_editors.csv', header=None)
authors_en = list(df[0])
print(len(authors_en), len(authors_hi))
common_authors = list(set(authors_hi) & set(authors_en))
print(common_authors)
