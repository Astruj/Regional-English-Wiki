import wiki_dump_parser as parser
import pandas as pd
import wikipediaapi
import hindi_readability
import pageviewapi


# this function reads the XML dump of wikipedia and outputs the processed data in a CSV file
def parse_dump(file_path):
    parser.xml_to_csv(file_path)


# this function returns number of revisions for an article
def get_number_of_revisions(article_name, filepath):
    chunksize = 10 ** 6
    revision_count = 0
    for chunk in pd.read_csv(filepath, quotechar='|', index_col=False, chunksize=chunksize):
        chunk = chunk[chunk['page_title'] == article_name]
        if not chunk.empty:
            revision_count += chunk.shape[0]

    return revision_count


# this function returns number of unique editors for an article
def get_number_of_unique_editors(article_name, filepath):
    chunksize = 10 ** 6
    authors_list = []
    for chunk in pd.read_csv(filepath, quotechar='|', index_col=False, chunksize=chunksize):
        chunk = chunk[chunk['page_title'] == article_name]
        if not chunk.empty:
            authors_list.extend(list(chunk['contributor_id']))

    return len(set(authors_list))


# this function returns total number of bytes edited for every revision of an article
def get_number_of_bytes_edited(article_name, filepath):
    chunksize = 10 ** 6
    total_byte_count = 0
    for chunk in pd.read_csv(filepath, quotechar='|', index_col=False, chunksize=chunksize):
        chunk = chunk[chunk['page_title'] == article_name]
        if not chunk.empty:
            for byte_count in list(chunk['bytes']):
                total_byte_count += byte_count

    return total_byte_count


# this function returns list of all the articles present in a category
def get_all_articles_in_a_category(category_name):
    category_name = "Category:"+category_name
    category_list = []
    wiki_wiki = wikipediaapi.Wikipedia('hi')
    cat = wiki_wiki.page(category_name)
    categorymembers = cat.categorymembers
    for category in categorymembers.values():
        if(category.ns == 0):
            category_list.append(category.title)

    return category_list


# this function returns readability score of an article
def get_readability_score(article_name):
    wiki_wiki = wikipediaapi.Wikipedia('hi')
    page = wiki_wiki.page(article_name)
    content = page.text
    return hindi_readability.Hindi(content).score()


# this function returns number of pageviews of an article
def get_number_of_pageviews(article_name):
    pageview_data = pageviewapi.per_article(
        'hi.wikipedia', article_name, start='20000101', end='20201020', granularity='monthly')
    pageview_count = 0
    for item in pageview_data['items']:
        pageview_count += item['views']

    return pageview_count


# this function returns ginni coefficient of a numpy array
def calculate_gini(array):
    mean_absolute_difference = np.abs(np.subtract.outer(array, array)).mean()
    relative_mean_absolute_difference = mean_absolute_difference/np.mean(array)
    gini_coefficient = 0.5 * relative_mean_absolute_difference
    return gini_coefficient


# this function calculates gini coefficient for an article based on revision distribution
def gini_coefficient(article_name, filepath):
    chunksize = 10 ** 6
    authors_list = []
    for chunk in pd.read_csv(filepath, quotechar='|', index_col=False, chunksize=chunksize):
        chunk = chunk[chunk['page_title'] == article_name]
        if not chunk.empty:
            authors_list.extend(list(chunk['contributor_id']))

    frequency_dict = collections.Counter(authors_list)
    frequency_array = np.array(list(frequency_dict.values()))
    gini = calculate_gini(frequency_array)
    return gini


# this function calculates gini coefficient for an article list based on revision distribution
def gini_coefficient_of_article_list(article_list, filepath):
    chunksize = 10 ** 6
    dict_authors_list = {k: [] for k in article_list}
    for chunk in pd.read_csv(filepath, quotechar='|', index_col=False, chunksize=chunksize):
        for article in article_list:
            new_chunk = chunk[chunk['page_title'] == article]
            dict_authors_list[article].extend(
                list(new_chunk['contributor_id']))

    gini_dict = {}
    for article in article_list:
        frequency_dict = collections.Counter(dict_authors_list[article])
        frequency_array = np.array(list(frequency_dict.values()))
        gini = calculate_gini(frequency_array)
        gini_dict[article] = gini

    return gini_dict
