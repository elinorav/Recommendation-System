import PySimpleGUI as sg
import tkinter as tk
from tkinter import *


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


def Title():
    lbl_result["text"] = "The Title is a great title"


def Keyword():
    lbl_result["text"] = "The Keywords is a great Keywords"


def Image():
    lbl_result["text"] ="The Image is a great Image"

if __name__ == '__main__':
  window = tk.Tk()

  lbl_titel = tk.Label(text="Recommendation-System", fg="red", height=3, font="Helvetica 15",)
  lbl_enter = tk.Label(text="enter url:", fg="black",font="Helvetica 12")
  entry_url = tk.Entry(fg="yellow", bg="black", width=50)
  btn_title = tk.Button(text="scan by Title", fg="black",font="Helvetica 10", command=Title)
  btn_keyword = tk.Button(text="scan by keyword", fg="black",font="Helvetica 10", command=Keyword)
  btn_image = tk.Button(text="scan by image", fg="black",font="Helvetica 10", command=Image)
  lbl_result = tk.Label()
  btn_exit = tk.Button(text="Quit", command=lambda root=window: quit(root))

  lbl_titel.pack(fill=tk.X)
  lbl_enter.place(x=0, y=50)
  entry_url.pack(fill=tk.X)
  btn_title.pack(fill=tk.X)
  btn_keyword.pack(fill=tk.X)
  btn_image.pack(fill=tk.X)
  lbl_result.pack()
  #btn_exit.pack(fill=tk.X)
  btn_exit.pack(side=tk.RIGHT)

  window.mainloop()

