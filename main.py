import tkinter as tk
from tk import *
import Ver1, Ver2, Ver3, Ver4
from Ver4 import *
from PIL import ImageTk, Image

def doTextInput():
  global text
  def back():
    txt.destroy()
    text.destroy()
    conf.destroy()
    back.destroy()
  txt = tk.Label(text="What is the seed for the program?")
  text = tk.Entry()
  conf = tk.Button(text="Confirm", command=set4Seed, relief=tk.GROOVE)
  back = tk.Button(text="Back", command=back, relief=tk.GROOVE)
  txt.pack()
  text.pack()
  conf.pack()
  back.pack()

def setTextSeed():
  global textSeed
  textSeed = int(text.get())

def set4Seed():
  setTextSeed()
  Ver4.seedVar = textSeed
  Ver4.positive()

root = tk.Tk()
root.resizable(0, 0)
root.geometry('1280x550')
root.title('Random Graph Generator')
frame_a = tk.Frame()
label = tk.Label(master=frame_a, text="Select the Generator Version You Want to Use:")
Version1 = tk.Button(master=frame_a, text="Version 1 (Newest)", width=15, height=2, fg='black', bg='white', command=Ver3.positive)
Version2 = tk.Button(master=frame_a, text="Version 2", width=10, height=2, fg='black', bg='white', command=Ver2.positive)
Version3 = tk.Button(master=frame_a, text="Version 3", width=10, height=2, fg='black', bg='white', command=Ver1.positive)
Version4 = tk.Button(master=frame_a, text="Version 4 (Oldest)", width=15, height=2, fg='black', bg='white', command=doTextInput)
image = ImageTk.PhotoImage(Image.open('./Images/Graph1.png'))
imageshow = tk.Label(image=image)
frame_a.pack()
label.pack(side=tk.TOP)
Version1.pack(side=tk.LEFT)
Version2.pack(side=tk.LEFT)
Version3.pack(side=tk.LEFT)
Version4.pack(side=tk.LEFT)
imageshow.pack(side=tk.BOTTOM)
root.mainloop
