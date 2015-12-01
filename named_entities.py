import os
import PyPDF2
import docx
import nltk

directory = r"C:\Users\Public\Documents\namedEntities"

full_text = []

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.pdf'):
            pdf_file_obj = open(os.path.join(root, file), 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            
            iter_var = 0
            while iter_var <= pdf_reader.numPages - 1:
                page_obj = pdf_reader.getPage(iter_var)
                full_text.append(page_obj.extractText())
                iter_var += 1
                
        elif file.endswith('.docx'):
            doc = docx.Document(os.path.join(root, file))
            for paragraph in doc.paragraphs:
                full_text.append(paragraph.text)

sentences = nltk.sent_tokenize(str(full_text))
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'PERSON':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names


entity_names = []
for tree in chunked_sentences:
    entity_names.extend(extract_entity_names(tree))

d = {}

# Print all entity names
for i in entity_names:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
        continue

# Print unique entity names
for w in sorted(d, key=d.get, reverse=True):
  print w, d[w]