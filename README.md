# Regional-English-Wiki
Difference between regional and English Wikipedia

## Download wiki dumps for the below languages:<br>
Hindi : https://dumps.wikimedia.your.org/hiwiki/20201001/<br>
Russian : https://dumps.wikimedia.your.org/ruwiki/20201020/<br>
German : https://dumps.wikimedia.your.org/dewiki/20201020/<br>
French : https://dumps.wikimedia.org/frwiki/20201220/<br>

## Install the following libraries:<br>
pip install kdap<br>
pip install pandas<br>
pip install wiki-dump-parser<br>
pip install readability<br>
pip install textstat<br>
pip install wikipedia<br>
pip install Wikipedia-API<br>
pip install matplotlib<br>

## Sample function usage in the project:
Maintain the directory structure of the project. Here filepath refers to filepath of extracted wiki dumps.
* import the respective language module<br>
  ```$ import german_wiki_module```
* parse the dump<br>
  ```$ german_wiki_module.parse_dump(filepath)```
* get number of revisions for an article<br>
  ```$ german_wiki_module.get_number_of_revisions(article_name, filepath)```
* get number of unique editors for an article<br>
  ```$ german_wiki_module.get_number_of_unique_editors(article_name, filepath)```
* get list of all the articles present in a category<br>
  ```$ german_wiki_module.get_all_articles_in_a_category(category_name)```
* get readability score of an article<br>
  ```$ german_wiki_module.get_readability_score(article_name)```
* get number of pageviews of an article<br>
  ```$ german_wiki_module.get_number_of_pageviews(article_name)```
