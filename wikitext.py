import wikipedia as wk
import wikipediaapi
# wk.set_lang('hi')
# page = wk.page('नागरिकता (संशोधन) अधिनियम, २०१९')
# # print(page.title)
# # print(page.url)
# print(page.categories)
# # print(page.content)

# page_list = wk.search('Citizenship (Amendment) Act, 2019')
# print(page_list)


wiki_wiki = wikipediaapi.Wikipedia('en')
def print_categorymembers(categorymembers, level=0, max_level=1):
        for c in categorymembers.values():
            print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)


cat = wiki_wiki.page("Category:Acts of the Parliament of India")
#print("Category members: Category:Physics")
print_categorymembers(cat.categorymembers)