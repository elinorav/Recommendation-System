import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "extract_title/https://www.calcalist.co.il/local_news/car/article/byalndbft?ref=ynet",{})
response = requests.get(BASE + "/extract_title", {'url' : "https://www.bbc.com/news/health-59488848"})
#response = requests.get(BASE + "extract_title/blabla",{})
print(response.text)
response = requests.get(BASE + "/extract_keywords", {'url' : "https://www.bbc.com/news/health-59488848"})
#print(response.text)
