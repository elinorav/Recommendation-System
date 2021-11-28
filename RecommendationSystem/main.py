import urllib.request

import spacy as spacy
import yake as yake
from bs4 import BeautifulSoup


# checks if str in part of a title or a header
def check_if_in_title(title, str):
    if str in title:
        return True
    return False


def check_if_in_header(htmlParse, h_i, str):
    headers = htmlParse.find_all(h_i)
    if (type(headers) == type(None)) or (len(headers) == 0):
        return False
    for t in headers:
        if str.lower() in t.text.lower():
            return True
    return False


if __name__ == '__main__':
    url = input('Please enter a URL of a lending page')
    print('You have entered:' + url)

    # url = 'https://www.bbc.com/storyworks/clear-sky-thinking-airbus-2021/airbus-2021-clear-sky-thinking' \
    #       '-?utm_source=taboola&utm_medium=native&tblci' \
    #       '=GiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyCLjFQojKLYzprtvuKHAQ' \
    #       '#tblciGiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyCLjFQojKLYzprtvuKHAQ'

    # opening the url for reading
    html = urllib.request.urlopen(url)

    # parsing the html file
    htmlParse = BeautifulSoup(html, 'lxml')
    title = htmlParse.find('title')

    # dictionary for score
    score_dict = {'title': 0.07, 'h1': 0.06, 'h2': 0.05, 'h3': 0.04,
                  'h4': 0.03, 'h5': 0.02, 'h6': 0.01}

    paragraphs = ""
    paragraph_tags = htmlParse.find_all('p')
    for p in paragraph_tags:
        paragraphs += str(p.text).lower()
    # print(paragraphs)

    kw_extractor = yake.KeywordExtractor()
    language = "en"
    max_ngram_size = 2
    deduplication_threshold = 0.9
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(paragraphs)
    res_list = []
    for kw in keywords:
        new_score = kw[1]
        if check_if_in_title(title.text.lower(), str(kw[0]).lower()):
            new_score = kw[1] * (1 - score_dict['title'])
        for i in range(1, 7):
            if check_if_in_header(htmlParse, 'h' + str(i), str(kw[0]).lower()):
                new_score = kw[1] * (1 - score_dict['h' + str(i)])
        new_tuple = (kw[0], new_score)
        res_list.append(new_tuple)

    print(keywords)
    print(res_list)
