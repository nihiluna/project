import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://wals.info/languoid")
soup = BeautifulSoup(page.text,'lxml')

outcome_csv = "lang_data.csv"
csv_writer = csv.writer(open(outcome_csv, 'w'))

for tr in soup.find_all('tr'):
    data = []
    for th in tr.find_all('th'):
    	data.append(th.text)
    if data:
    	print("Inserting headers: {} ".format(','.join(data)))
    	csv_writer.writerow(data)
    	continue
   
    for td in tr.find_all('td'):
    	data.append(td.text.strip())
    if data:
    	print("Inserting Table Data: {} ".format(','.join(data)))
    	data.append(td.text.strip())
    csv_writer.writerow(data)
