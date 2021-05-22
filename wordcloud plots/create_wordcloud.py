import csv
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

reader = csv.reader(open('depth.csv', 'r', newline='\n'))
d = {}
for k, v in reader:
    d[k] = float(v)
    print(d[k])

wordcloud = WordCloud(width=1400, height=700, max_words=1628, background_color='white', relative_scaling=0.75,
                      normalize_plurals=False).generate_from_frequencies(d)

plt.figure(dpi=300)
plt.tight_layout(pad=0)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
# plt.show()
# plt.savefig("result.png", dpi=300)
plt.savefig('depth.png', dpi=600, facecolor='k', bbox_inches='tight')
