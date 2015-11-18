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



		subjects = tree.xpath('/video_metadata/subjects/subject')
		print subjects

		transcript = tree.xpath('/video_metadata/transcript')[0].text
		text = nltk.word_tokenize(transcript)
		clean_text = [w.lower() for w in text if w.isalnum()]
		clean_text = [w for w in clean_text if w not in stopwords.words('english')]
		clean_text = [w for w in clean_text if w not in stopwords_list]

		fdist = nltk.FreqDist(clean_text)
		for i in fdist.most_common(5):

			if i[0] in clean_title:
				print 'FOUND ONE', i