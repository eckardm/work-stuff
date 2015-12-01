import os
import logging
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

for filename in os.listdir(r"C:\Users\eckardm\work-stuff\regents-proceedings"):
    with open(filename, mode="r") as f:
        # load id->word mapping (the dictionary)
        id2word = gensim.corpora.Dictionary.load_from_text(f.read())
        # load corpus iterator
        mm = gensim.corpora.MmCorpus('wiki_en_tfidf.mm')
        # extract 100 LDA topics, using 20 full passes, (batch mode) no online updates
        lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=0, passes=20)
        print filename
        print lda
