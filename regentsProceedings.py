import requests
from bs4 import BeautifulSoup

umregprocs_data = requests.get("http://quod.lib.umich.edu/cgi/t/text/text-idx?page=browse&c=umregproc")
umregprocs_soup = BeautifulSoup(data.text)

for umregproc_url in soup.find_all("a") if umregproc_url.endswith("view=toc"):
	umregproc_data = requests.get(umregproc_url)
	umregproc_soup = BeautifulSoup(regents_proceeding_data.text)
		
	for page_url in soup.find_all("a") if page_url.endswith("view=pdf"):
		ocr_url = page_url.replace("pdf", "text")
		ocr_data = requests.get(ocr_url)
		ocr_soup = BeautifulSoup(ocr_data.text)

		ocr = ocr_soup.find("div", {"id": "pvdoccontent"}).text
		
		print ocr
