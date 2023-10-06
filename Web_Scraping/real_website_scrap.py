from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://djinni.co/jobs/?primary_keyword=Python").text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

# experience = soup.find_all('span', class_='nobr')
test2 = soup.find('div', class_='job-list-item__job-info').find_all(class_='nobr')
print(test2[1].text[3:])