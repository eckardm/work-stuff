import os
import textract
from nltk.tag import StanfordNERTagger

full_text = ""

for root, _, files in os.walk(r"C:\Users\Public\Documents\namedEntities"):
    for name in files:
        text = textract.process(os.path.join(root, name))
        full_text += text
        
st = StanfordNERTagger("english.all.3class.distsim.crf.ser.gz")
st.tag(full_text.split())
