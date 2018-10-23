import requests
from bs4 import BeautifulSoup
import csv
import pandas 

with open('namelist.csv','r')as f:
    rows=csv.reader(f)
    for header in rows:
        print(header)

list=[]

for i in range(1,len(header)):
    url='https://github.com/{0}'.format(header[i])
    r=requests.get(url).text
    data=BeautifulSoup(r,"html.parser")
    information=data.find_all('rect')
    for j in range(330,len(information)):
        list.append([header[i],information[j]['data-date'],information[j]['data-count']])

# (username, datetime, contributions)
with open('contribution.csv','w',newline='') as f:
    writer=csv.writer(f)
    header=['username','datetime','contribution']
    writer.writerow(header)
    for i in range(0,len(list)):
        writer.writerow([list[i][0],list[i][1],list[i][2]])

