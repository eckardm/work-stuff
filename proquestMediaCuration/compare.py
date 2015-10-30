import os
from os.path import join
from lxml import etree
import nltk
from nltk.tokenize import RegexpTokenizer
import csv
from sklearn.feature_extraction.text import TfidfVectorizer

path = r'C:\Users\Public\Documents\proquestMediaCuration'

willis_ward = []
bhl = []
post_texas = []
arthur_miller = []
jfk = []
cornflower = []
esther_holmes = []
mlk = []
racism_sexism = []

for filename in os.listdir(path):
	if filename.endswith('.xml'):

		dictionary = {}

		dictionary["filename"] = filename

		tree = etree.parse(join(path, filename))

		titles = tree.xpath('/video_metadata/title')
		title = titles[0].text.encode('utf-8').strip()
		dictionary["title"] = title

		if '(automated transcription)' in title:
			dictionary["automated_transcription"] = True
		else:
			dictionary["automated_transcription"] = False
		
		transcripts = tree.xpath('/video_metadata/transcript')
		transcript_raw = transcripts[0].text
		dictionary["raw"] = transcript_raw

		tokenizer = RegexpTokenizer(r'\w+')
		transcript_text = tokenizer.tokenize(transcript_raw)
		dictionary["text"] = transcript_text

		transcript_clean_text = [w.lower() for w in transcript_text]
		dictionary["clean_text"] = transcript_clean_text

		if 'Ward' in title:
			willis_ward.append(dictionary)
		elif 'Bentley' in title:
			bhl.append(dictionary)
		elif 'Post' in title:
			post_texas.append(dictionary) 
		elif 'Miller' in title:
			arthur_miller.append(dictionary)
		elif 'Kennedy' in title:
			jfk.append(dictionary)
		elif 'Cornflower' in title:
			cornflower.append(dictionary)
		elif 'Holmes' in title:
			esther_holmes.append(dictionary)
		elif 'Luther King' in title:
			mlk.append(dictionary)
		elif 'Racism' in title:
			racism_sexism.append(dictionary)

list_sho = [willis_ward, bhl, post_texas, arthur_miller, jfk, cornflower, esther_holmes, mlk, racism_sexism]

compare_total = 0

def compare(pair, compare_total):
	counter = 0
	for w in set(sorted(pair)[1]["clean_text"]):
		if w in set(sorted(pair)[0]["clean_text"]):
			counter += 1
	print sorted(pair)[1]["title"]
	a = float(counter) / float(len(set(sorted(pair)[1]["clean_text"]))) * 100
	print a
	return a
	print '\n'

cosine_similarity_total = 0

def cosine_similarity(pair, cosine_similarity_total):
	vect = TfidfVectorizer(min_df=1)
	tfidf = vect.fit_transform([sorted(pair)[1]["raw"], sorted(pair)[0]["raw"]])
	print sorted(pair)[1]["title"]
	a = (tfidf * tfidf.T).A[0][1] * 100
	print a
	return a
	print '\n'

bigrams_total = 0

def bigrams(pair, bigrams_total):
	counter = 0
	for i in set(nltk.bigrams(sorted(pair)[1]["text"])):
		print i
		if i in set(nltk.bigrams(sorted(pair)[0]["text"])):
			counter += 1
		print sorted(pair)[1]["title"]
		a = float(counter) / len(set(nltk.bigrams(sorted(pair)[1]["text"]))) * 100
		print a
		return a
		print '\n'

print '\n\n'

print 'COMPARING SETS\n'
for list_dai in list_sho:
	compare_total += compare(list_dai, compare_total)
print '\nAverage: ', compare_total / 9

print '\n\n'

print 'COSINE SIMILARITY\n'
for list_dai in list_sho:
	cosine_similarity_total += cosine_similarity(list_dai, cosine_similarity_total)
print '\nAverage: ', cosine_similarity_total / 9

print '\n\n'

print 'BIGRAMS\n'
for list_dai in list_sho:
	bigrams_total += bigrams(list_dai, bigrams_total)
print '\nAverage: ', bigrams_total / 9
