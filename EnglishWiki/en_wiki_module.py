import readability
from langdetect import detect
from textstat.textstat import textstat
import kdap
import wikipediaapi
import os
import pageviewapi


# this function returns list of all the articles present in a category
def get_all_articles_in_a_category(category):
    category = "Category:"+category
    category_list = []  
    wiki_wiki = wikipediaapi.Wikipedia('en')
    cat = wiki_wiki.page(category)
    categorymembers = cat.categorymembers
    for c in categorymembers.values():
        if(c.ns==0):
            category_list.append(c.title)

    return(category_list)


#download english dump in knolml format
def download_articles_of_cotegory(title,dir):
    knol = kdap.knol()
    knol.get_wiki_article(title,dir)

# this function returns number of unique editors for an article
def get_number_of_unique_editors(article_name, filepath):
    k = kdap.analysis.knol()
    editors = k.get_editors(dir_path = filepath+'/'+'output')
    #print("Number Of Unique Editors for article -",article_name," :",len(set(editors[article_name])),'\n')
    return len(set(editors[article_name]))

def get_list_of_unique_editors(article_name, filepath):
    k = kdap.analysis.knol()
    editors = k.get_editors(dir_path = filepath+'/'+'output')
    editors = list(set(editors[article_name]))
    return editors


# this function returns readability score of an article
def get_readability_score(article_name):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(article_name)
    text = page.text

    #Language
    language = detect(text)
    
    #Readability_Using_Textstat_lib
    rd1 = textstat.flesch_reading_ease(text)
    #print("Readability 1 :",rd1)
    
    rd2 = 0
    #Readability_Using_Readability_lib
    d = readability.getmeasures(text,lang = language)
    rd2 = d['readability grades']['FleschReadingEase']
    #print("Readability 2:",rd2)

    #Average_Readbility
    av = (rd1+rd2)/2
    #print("Average Readability :", av )
    
    return av


# this function returns number of pageviews of an article
def get_number_of_pageviews(article_name):
    pageview_data = pageviewapi.per_article(
        'en.wikipedia', article_name, start='20000101', end='20201020', granularity='monthly')
    pageview_count = 0
    for item in pageview_data['items']:
        pageview_count += item['views']

    return pageview_count

def get_number_of_revisions(filepath):
    knol = kdap.analysis.knol()
    revisions = knol.get_num_instances(dir_path= filepath+'/'+'output')

    return revisions

# # this function does revision wise analysis
# def frame_analysis(path):
#     k = kdap.analysis.knol()
#     frames = k.frame(dir_path = path+'/'+'output')
#     frames = list(frames)
#     print(frames[118].get_title())
#     print(len(frames))