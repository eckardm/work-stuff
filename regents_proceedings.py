import requests
from bs4 import BeautifulSoup
import time

# i'm a concientious scraper
headers = {"user-agent": "UMRegProc Scraper, eckardm@umich.edu"}
umregprocs_data = requests.get("http://quod.lib.umich.edu/cgi/t/text/text-idx?page=browse&c=umregproc", headers=headers)
umregprocs_soup = BeautifulSoup(umregprocs_data.text)

for umregproc_url in umregprocs_soup(href=True):
    if umregproc_url['href'].endswith("view=toc"):
        umregproc_data = requests.get(umregproc_url['href'])
        umregproc_soup = BeautifulSoup(umregproc_data.text)
        
        title = umregproc_soup("title")[0].text
        print title
    
        for page_url in umregproc_soup(href=True):
            if page_url['href'].endswith("view=pdf"):
                
                ocr_url = page_url['href'].replace("pdf", "text")
                ocr_data = requests.get(ocr_url)
                ocr_soup = BeautifulSoup(ocr_data.text)

                ocr = ocr_soup(id="pvdoccontent")[0].text.encode('utf-8')
                
                print ocr
                
                with open(title + ".txt", mode="a") as f:
                    f.write(ocr)
                
                # i'm a concientious scraper
                time.sleep(1)
