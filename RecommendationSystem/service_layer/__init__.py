import PySimpleGUI as sg
import tkinter as tk
import system_service_layer


def Analysis():
  lbl_result["text"] = "The Keywords is a great Keywords"

def Title():

    lbl_result["text"] ="The Title is "+ url_var.get()

def Keyword():
    lbl_result["text"] = "The Keywords is " + url_var.get()

# def Image():
#     lbl_result["text"] ="The Image is "+ url_var.get()
#

if __name__ == '__main__':

  window = tk.Tk()
  url_var = tk.StringVar()
  url_var.set("")

  lbl_titel = tk.Label(text="Recommendation-System", fg="red", height=3, font="Helvetica 15").pack(fill=tk.X)
  lbl_enter = tk.Label(text="enter url:", fg="black", font="Helvetica 12").place(x=0, y=50)
  entry_url = tk.Entry(textvariable = url_var,fg="yellow", bg="black", width=50).pack(fill=tk.X)

  btn_title = tk.Button(text="scan by Title", fg="black", font="Helvetica 10", command=Title).pack(fill=tk.X)
  btn_keyword = tk.Button(text="scan by keyword", fg="black", font="Helvetica 10", command=Keyword).pack(fill=tk.X)
  #btn_image = tk.Button(text="scan by image", fg="black", font="Helvetica 10", command=Image).pack(fill=tk.X)
  lbl_result = tk.Label()
  btn_exit = tk.Button(text="Quit", command=lambda root=window: quit(root))

  lbl_result.pack()
  btn_exit.pack(side=tk.RIGHT)

  window.mainloop()



# class App(tk.Frame):
#   def __init__(self, master):
#     super().__init__(master)
#     self.pack()
#
#     self.entrythingy = tk.Entry()
#     self.entrythingy.pack()
#
#     # Create the application variable.
#     self.contents = tk.StringVar()
#     # Set it to some value.
#     self.contents.set("this is a variable")
#     # Tell the entry widget to watch this variable.
#     self.entrythingy["textvariable"] = self.contents
#
#     # Define a callback for when the user hits return.
#     # It prints the current value of the variable.
#     self.entrythingy.bind('<Key-Return>',
#                           self.print_contents)
#
#   def print_contents(self, event):
#     print("Hi. The current entry content is:",
#           self.contents.get())
#   root = tk.Tk()
#   myapp = App(root)
#   myapp.mainloop()