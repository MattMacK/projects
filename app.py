from bs4 import BeautifulSoup
import urllib, csv, os, datetime, urllib.request, re, sys

theurl = "https://www.wunderground.com/history/airport/KSAT/2016/05/08/DailyHistory.html?req_city=San%20Antonio&req_state=TX&reqdb.zip=78269&reqdb.magic=1&reqdb.wmo=99999"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

mean = soup.find_all('tr')[2].find_all('td')[1].find(attrs={"class":"wx-value"}).text
max = soup.find_all('tr')[3].find_all('td')[1].find(attrs={"class":"wx-value"}).text
min = soup.find_all('tr')[4].find_all('td')[1].find(attrs={"class":"wx-value"}).text

print("Mean = ", mean)
print("Max = ", max)
print("Min = ", min)