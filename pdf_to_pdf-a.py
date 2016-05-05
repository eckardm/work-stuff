import os
import ghostscript

path = os.path.join("Q:", "Homefolders", "eckardm", "Desktop", "Sample Textual Content")

for name in os.listdir(path):

    if not name.endswith("_PDFA.pdf") and name.replace(".pdf", "_PDFA.pdf") not in os.listdir(path):

        arguments = [
            "-dPDFA", 
            "-dBATCH", 
            "-dNOPAUSE", 
            "-sDEVICE=pdfwrite", 
            "-sOutputFile=" + os.path.join(path, name.replace(".pdf", "_PDFA.pdf")),
            os.path.join(path, name)
        ]
        
        ghostscript.Ghostscript(*arguments)
