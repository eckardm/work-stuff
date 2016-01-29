import os
from bs4 import BeautifulSoup

oral_history_interviews = [name for name in os.listdir("substance.abuse.history") if "oral_history_interviews&findAll=true&mode=single&recordID=" in name and "&nextMode=list" not in name]

metadata_list = []

for name in oral_history_interviews:

    with open(os.path.join("substance.abuse.history", name), mode="r") as input:
        soup = BeautifulSoup(input, "lxml")
        
        metadata_dict = {}
        
        interviewee = soup.find(text="Interviewee: ").parent.parent.find_next_siblings("td")[0].text.strip()
        if interviewee.endswith("Retired, NIDA Intramural Research Program, Baltimore, MD"):
            interviewee = "Wallace Pickworth (Retired, NIDA Intramural Research Program, Baltimore, MD)"
        if interviewee.endswith("University of Kentucky"):
            interviewee = "Jewell Sloan (University of Kentucky)"
        metadata_dict["interviewee"] = interviewee  
        
        biographical_note = ""
        
        interviewer = soup.find(text="Interviewer(s): ").parent.parent.find_next_siblings("td")[0].text.strip()
        if len(interviewer) > 0:
            metadata_dict["interviewer"] = interviewer        
            
        date = ""
        
        suggested_citation = ""
        
        keywords = ""
        
        metadata_list.append(metadata_dict)
