# PDF Text Extractor
def extracting_text_from_pdfs(pdf_file):
    
    import PyPDF2
    
    pdf_file_object = open(pdf_file, mode="rb")
    pdf_reader = PyPDF2.reader(pdf_file_object)
    
    page_object = pdf_reader.getPage(0)    
    print(page_object.extractText())

# HTML Text Extractor

# Powerpoint Text Extractor

# Word Text Extractor

# JPEG

extracting_text_from_pdfs("Help-HTRC-OpenOpen-corpus.pdf")