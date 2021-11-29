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


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("900x400")
    url_var = tk.StringVar()
    url_var.set("")

    lbl_titel = tk.Label(text="Recommendation-System", fg="red", height=4, font="Helvetica 20").pack(fill=tk.X)
    lbl_enter = tk.Label(text="Please enter a URL of a landing page:", fg="black", font="Helvetica 17").place(x=0, y=100)
    entry_url = tk.Entry(textvariable=url_var, fg="yellow", bg="black", width=50).pack(fill=tk.X, ipady=10)

    btn_title = tk.Button(text="scan for title", fg="black", font="Helvetica 15", command=Title).pack(fill=tk.X)
    btn_keyword = tk.Button(text="scan for keywords", fg="black", font="Helvetica 15", command=Keyword).pack(fill=tk.X)
    # btn_image = tk.Button(text="scan by image", fg="black", font="Helvetica 10", command=Image).pack(fill=tk.X)
    lbl_result = tk.Label(fg="blue", font="Helvetica 17")
    btn_exit = tk.Button(text="Quit", command=lambda root=window: quit(root))

    lbl_result.pack(fill=tk.X)
    btn_exit.pack(side=tk.BOTTOM)

    window.mainloop()