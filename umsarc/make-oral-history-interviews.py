import os
from bs4 import BeautifulSoup
import re
from lxml import etree

print "Getting metadata..."

oral_history_interviews = [name for name in os.listdir("substance.abuse.history") if "oral_history_interviews&findAll=true&mode=single&recordID=" in name and "&nextMode=list" not in name]

metadata = []

for name in oral_history_interviews:

    with open(os.path.join("substance.abuse.history", name), mode="r") as oral_history_interview:
        soup = BeautifulSoup(oral_history_interview, "lxml")
        
        metadata_dict = {}
        
        metadata_dict["name"] = name
        
        interviewee = soup.find(text="Interviewee: ").parent.parent.find_next_siblings("td")[0].text.strip()
        if interviewee.endswith("Retired, NIDA Intramural Research Program, Baltimore, MD"):
            interviewee = "Wallace Pickworth (Retired, NIDA Intramural Research Program, Baltimore, MD)"
        if interviewee.endswith("University of Kentucky"):
            interviewee = "Jewell Sloan (University of Kentucky)"
        metadata_dict["interviewee"] = interviewee  
        
        biographical_note = soup.find(text=re.compile("^Biographical"))
        if biographical_note:
            biographical_note = str(biographical_note.parent.parent.find_next_siblings("td")[0].encode("utf-8")).replace("<td>", "").replace("</td>", "")
            metadata_dict["biographical_note"] = biographical_note
        
        interviewer = soup.find(text="Interviewer(s): ").parent.parent.find_next_siblings("td")[0].text
        if len(interviewer) > 0:
            metadata_dict["interviewer"] = interviewer        
            
        date = soup.find(text="Date: ")
        if date:
            date = date.parent.parent.find_next_siblings("td")[0].text.strip()
            metadata_dict["date"] = date
        
        suggested_citation = soup.find(text=re.compile("^Suggested"))
        if suggested_citation:
            suggested_citation = suggested_citation.parent.parent.find_next_siblings("td")[0].text
            metadata_dict["suggested_citation"] = suggested_citation
        
        keywords = soup.find(text="Keywords:")
        if keywords:
            keywords = keywords.parent.parent.find_next_siblings("td")[0].text
            metadata_dict["keywords"] = keywords
            
        metadata.append(metadata_dict)
        
print "Getting transcripts..."

for metadatum in metadata:

    with open(os.path.join("substance.abuse.history", metadatum["name"].replace("oral_history_interviews&findAll=true&mode=single&recordID=", "manage_interviews&mode=single&recordID=")), mode="r") as oral_history_interview:
        soup = BeautifulSoup(oral_history_interview, "lxml")
        
        possible_transcripts = soup.find_all("textarea")
        for possible_transcript in possible_transcripts:
            if possible_transcript["name"].startswith("Transcript"):
                metadatum["transcript"] = possible_transcript.text.encode("utf-8")
                
print "Making PDFs..."
