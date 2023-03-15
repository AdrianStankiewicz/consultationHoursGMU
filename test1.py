import requests
from bs4 import BeautifulSoup

# Make a GET request to the URL
url = "https://we.umg.edu.pl/ktm/konsultacje"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

dirty_h3s = soup.find_all('h3')

professors = []
rooms = []

for dirty_h3 in dirty_h3s:
    professor = []

    for child in dirty_h3:
        if child.name == 'br':
            continue

        child = child.string.replace('\t', '').replace('\n', '')

        if 'pok.' in child:
            rooms.append(child)
        else:
            professor.append(child)
        
    professors.append(professor)

print('Count professors: ' + str(len(professors)))
print(professors)
print('=================')
print('Count rooms: ' + str(len(rooms)))
print(rooms)