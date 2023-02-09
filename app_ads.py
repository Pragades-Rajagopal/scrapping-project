from bs4 import BeautifulSoup
from pathlib import Path
import csv

PATH = Path(__file__).parent
HTML_PATH = PATH.joinpath('./html').resolve()
EXPORTS_PATH = PATH.joinpath('./exports').resolve()

html = HTML_PATH.joinpath('ads_interests.html')
csv_file = EXPORTS_PATH.joinpath('ads_interests.csv')

soup = BeautifulSoup(open(html), 'html.parser')
# print(soup)

interests = soup.find_all('td', {'class' : '_2pin _a6_q'})
result = []

for interest in interests:
    result.append({'Tag': 'Interest', 'Value': interest.find('div').find('div').contents[0]})

with open(csv_file, 'w') as f:
    try:
        fieldnames = ['Tag', 'Value']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in result:
            writer.writerow(r)

        print('CSV is prepared')

    except Exception as e:
        print('Exiting with error')

# print(result)
