from urllib.request import urlopen
import PySimpleGUI as sg
import tkinter as tk

def Title():
    page = urlopen(url_var.get())
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    lbl_result["text"] = title

def Keyword():
    page = urlopen(url_var.get())
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    lbl_result["text"] = html


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

    # landing_page = input('Please enter a URL of a lending page')
    # print('You have entered:' + landing_page)
    # page = urlopen(landing_page)
    # html_bytes = page.read()
    # html = html_bytes.decode("utf-8")
    # print(html)
    #
    #
    # title_index = html.find("<title>")
    # start_index = title_index + len("<title>")
    # end_index = html.find("</title>")
    # title = html[start_index:end_index]
    # print('The title of the page is: ' + title)


