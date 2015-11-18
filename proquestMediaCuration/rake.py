import RAKE
import os
from os.path import join
from lxml import etree
import re
import nltk
from nltk.corpus import stopwords

path = r'C:\Users\Public\Documents\proquestMediaCuration'

for filename in os.listdir(path):
    if filename.endswith('.xml'):
        tree = etree.parse(join(path, filename))
        
        title = tree.xpath('/video_metadata/title')[0].text

        subjects = tree.xpath('/video_metadata/subjects/subject')
        
        transcript = tree.xpath('/video_metadata/transcript')[0].text
        no_brackets = re.sub(r'\[(.*)\]', '', transcript)
        text = nltk.word_tokenize(no_brackets)
        
        Rake = RAKE.Rake('SmartStoplist.txt')


        with open(join(path, 'topicModeling.txt'), 'a') as t:
            t.write(title)
            t.write('\n')
            t.write('Proquest Subjects')
            t.write('\n')
            for subject in subjects:
                t.write(subject.text)
                t.write('\n')
            t.write('RAKE Subjects')
            t.write('\n')
            for i in Rake.run(no_brackets):
                if len(i[0].split(' ')) <= 5 and i[1] > 6:
                    t.write(i[0])
                    t.write('\n')
            t.write('\n')


