from imdbpie import Imdb

imdb = Imdb()

#for Stranger Things
 #takes the first 10 reviews on imdb and prints them into their separate files
for i in range(10):
    filename = 'review_{}.txt'.format(i)
    file = open(filename, 'w', encoding='utf8')
    file.write(imdb._get_reviews_data('tt4574334')[i]['text'])
    file.close()

#takes all the separate reviews and combines them into 1 composite file called strangerthings_reviews
filenames = ['review_0.txt', 'review_1.txt', 'review_2.txt', 'review_3.txt',
 'review_4.txt', 'review_5.txt', 'review_6.txt', 'review_7.txt', 'review_8.txt', 'review_9.txt']
with open('strangerthings_reviews.txt', 'w') as outfile: 
    for fname in filenames:
        with open(fname) as infile:
            content = infile.read().replace('\n', '')
            outfile.write(content)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

sentence = open('strangerthings_reviews.txt', 'r', encoding='utf8').read()

score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)
