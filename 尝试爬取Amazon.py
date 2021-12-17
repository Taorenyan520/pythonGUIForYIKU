import requests
url = 'https://www.amazon.com/s?k=Bamboo+basket&ref=nb_sb_noss'
date = requests.get(url).text
print(date)