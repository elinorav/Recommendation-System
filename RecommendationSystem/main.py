import urllib.request
import spacy as spacy
import yake as yake
from bs4 import BeautifulSoup
from urllib.request import urlopen
import PySimpleGUI as sg
import tkinter as tk
import business_layer
from business_layer.recoSystem import RecoSystem

#https://www.calcalist.co.il/local_news/car/article/byalndbft?ref=ynet
def Title():
    reco=RecoSystem()
    x, title = reco.scan_landing_page(url_var.get())
    lbl_result["text"] = title.text

def Keyword():
    reco = RecoSystem()
    keyword =reco.extract_keywords_from_landing_page(url_var.get())
    lbl_result["text"] = keyword


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
    window = tk.Tk()
    url_var = tk.StringVar()
    url_var.set("")

    lbl_titel = tk.Label(text="Recommendation-System", fg="red", height=3, font="Helvetica 15").pack(fill=tk.X)
    lbl_enter = tk.Label(text="Please enter a URL of a lending page:", fg="black", font="Helvetica 12").place(x=0, y=50)
    entry_url = tk.Entry(textvariable=url_var, fg="yellow", bg="black", width=50).pack(fill=tk.X)

    btn_title = tk.Button(text="scan by Title", fg="black", font="Helvetica 10", command=Title).pack(fill=tk.X)
    btn_keyword = tk.Button(text="scan by keyword", fg="black", font="Helvetica 10", command=Keyword).pack(fill=tk.X)
    # btn_image = tk.Button(text="scan by image", fg="black", font="Helvetica 10", command=Image).pack(fill=tk.X)
    lbl_result = tk.Label()
    btn_exit = tk.Button(text="Quit", command=lambda root=window: quit(root))

    lbl_result.pack()
    btn_exit.pack(side=tk.RIGHT)

    window.mainloop()











    # url = input('Please enter a URL of a lending page')
    # print('You have entered:' + url)
    #
    # # url = 'https://www.bbc.com/storyworks/clear-sky-thinking-airbus-2021/airbus-2021-clear-sky-thinking' \
    # #       '-?utm_source=taboola&utm_medium=native&tblci' \
    # #       '=GiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyCLjFQojKLYzprtvuKHAQ' \
    # #       '#tblciGiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyCLjFQojKLYzprtvuKHAQ'
    #
    # # opening the url for reading
    # html = urllib.request.urlopen(url)
    #
    # # parsing the html file
    # htmlParse = BeautifulSoup(html, 'lxml')
    # title = htmlParse.find('title')
    #
    # # dictionary for score
    # score_dict = {'title': 0.07, 'h1': 0.06, 'h2': 0.05, 'h3': 0.04,
    #               'h4': 0.03, 'h5': 0.02, 'h6': 0.01}
    #
    # paragraphs = ""
    # paragraph_tags = htmlParse.find_all('p')
    # for p in paragraph_tags:
    #     paragraphs += str(p.text).lower()
    # # print(paragraphs)
    #
    # kw_extractor = yake.KeywordExtractor()
    # language = "en"
    # max_ngram_size = 2
    # deduplication_threshold = 0.9
    # numOfKeywords = 20
    # custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
    #                                             top=numOfKeywords, features=None)
    # keywords = custom_kw_extractor.extract_keywords(paragraphs)
    # res_list = []
    # for kw in keywords:
    #     new_score = kw[1]
    #     if check_if_in_title(title.text.lower(), str(kw[0]).lower()):
    #         new_score = kw[1] * (1 - score_dict['title'])
    #     for i in range(1, 7):
    #         if check_if_in_header(htmlParse, 'h' + str(i), str(kw[0]).lower()):
    #             new_score = kw[1] * (1 - score_dict['h' + str(i)])
    #     new_tuple = (kw[0], new_score)
    #     res_list.append(new_tuple)
    #
    # print(keywords)
    # print(res_list)