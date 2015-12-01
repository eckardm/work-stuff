import requests
from bs4 import BeautifulSoup
from tqdm import *
import time
import os

'''
# i'm a concientious scraper
headers = {"user-agent": "UMRegProc Scraper, eckardm@umich.edu"}
umregprocs_data = requests.get("http://quod.lib.umich.edu/cgi/t/text/text-idx?page=browse&c=umregproc", headers=headers)
umregprocs_soup = BeautifulSoup(umregprocs_data.text)

for umregproc_url in umregprocs_soup(href=True):
    if umregproc_url['href'].endswith("view=toc"):
        umregproc_data = requests.get(umregproc_url['href'])
        umregproc_soup = BeautifulSoup(umregproc_data.text)
        
        title = umregproc_soup("title")[0].text
    
        for page_url in tqdm(umregproc_soup(href=True), desc=title):
            if page_url['href'].endswith("view=pdf"):
                
                page = page_url.text
                
                ocr_url = page_url['href'].replace("pdf", "text")
                ocr_data = requests.get(ocr_url)
                ocr_soup = BeautifulSoup(ocr_data.text)
                
                ocr = ocr_soup(id="pvdoccontent")[0].text.encode('utf-8')
            
                with open(title + ".txt", mode="a") as f:
                    f.write(ocr)
                
                # i'm a concientious scraper
                time.sleep(1)'''

for filename in os.listdir(r"C:\Users\eckardm\work-stuff\regents-proceedings"):
    if filename.endswith(".txt"):
        with open(filename, mode="r") as f_in:
            with open("Proceedings of the Board of Regents.txt", mode="a") as f_out:
                f_out.write(f_in.read())
