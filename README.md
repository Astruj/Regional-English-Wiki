# Regional-English-Wiki
Difference between regional and English Wikipedia

Download wiki dumps for the below languages:
Hindi : https://dumps.wikimedia.your.org/hiwiki/20201001/
Russian : https://dumps.wikimedia.your.org/ruwiki/20201020/
German : https://dumps.wikimedia.your.org/dewiki/20201020/
French : https://dumps.wikimedia.org/frwiki/20201220/

Install the following libraries:
pip install kdap
pip install pandas
pip install wiki-dump-parser
pip install readability
pip install textstat
pip install wikipedia
pip install Wikipedia-API
pip install matplotlib

Sample function usage in the project:
Maintain the directory structure of the project. Here filepath refers to filepath of extracted wiki dumps.
# import the respective language module
  import german_wiki_module
# parse the dump
  german_wiki_module.parse_dump(filepath)
# get number of revisions for an article
  german_wiki_module.get_number_of_revisions(article_name, filepath)
# get number of unique editors for an article
  german_wiki_module.get_number_of_unique_editors(article_name, filepath)
# get list of all the articles present in a category
  german_wiki_module.get_all_articles_in_a_category(category_name)
# get readability score of an article
  german_wiki_module.get_readability_score(article_name)
# get number of pageviews of an article
  german_wiki_module.get_number_of_pageviews(article_name)
