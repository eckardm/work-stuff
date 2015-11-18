import os
from os.path import join
from lxml import etree
import nltk
from constants import stopwords_list
from nltk.corpus import stopwords



path = r'C:\Users\Public\Documents\proquestMediaCuration'



for filename in os.listdir(path):
	if filename.endswith('.xml'):

		tree = etree.parse(join(path, filename))

		title = tree.xpath('/video_metadata/title')[0].text
		print title
		title_text = nltk.word_tokenize(title)
		clean_title = [w.lower() for w in title_text if w.isalnum()]
		clean_title = [w for w in clean_title if w not in stopwords.words('english')]
		clean_title = [w for w in clean_title if w not in stopwords_list]
		clean_title_bigrams = nltk.bigrams(clean_title)
		clean_title_trigrams = nltk.trigrams(clean_title)
		for i in clean_title_trigrams:
			print i



		subjects = tree.xpath('/video_metadata/subjects/subject')
		#print subjects

		transcript = tree.xpath('/video_metadata/transcript')[0].text
		text = nltk.word_tokenize(transcript)
		clean_text = [w.lower() for w in text if w.isalnum()]
		clean_text = [w for w in clean_text if w not in stopwords.words('english')]
		clean_text = [w for w in clean_text if w not in stopwords_list]
		clean_text_bigrams = nltk.bigrams(clean_text)
		clean_text_trigrams = nltk.trigrams(clean_text)


		fdist_trigrams = nltk.FreqDist(clean_text_trigrams)
		top_ten_trigrams = fdist_trigrams.most_common(10)
		for i in top_ten_trigrams:
			print i
			if i in clean_title_trigrams:
				print 'FOUND TRIGRAM', i


		fdist_bigrams = nltk.FreqDist(clean_text_bigrams)
		top_ten_bigrams = fdist_bigrams.most_common(10)
		for i in top_ten_bigrams:
			if i in clean_title_bigrams and i[0] not in clean_title_trigrams and i[1] not in clean_title_trigrams:
				print 'FOUND BIGRAM', i

		fdist = nltk.FreqDist(clean_text)
		top_ten = fdist_trigrams.most_common(10)
		for i in top_ten:
			if i[0] in clean_title and i not in clean_title_bigrams:
				print 'FOUND ONE', i