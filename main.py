import tkinter

from gtts import gTTS
from playsound import playsound
from tkinter import *


def playText():
    myText = textEntry.get()
    language = 'en'
    obj = gTTS(text=myText, lang=language, slow=False)
    obj.save("text.mp3")
    playsound("text.mp3")


window = Tk()
window.title('Text-To-Speech')
window.geometry('700x500')
window.config(background="grey")

textLabel = Label(window, text="Text-To-Speech", font=("Comic Sans", 40), background="grey")
textLabel.pack()

textCanvas = tkinter.Canvas(window, width=400, height=300)
textCanvas.pack()

textEntry = tkinter.Entry (window)
textCanvas.create_window(200, 140, window=textEntry)

submitButton = tkinter.Button(text='Submit Text', command=playText)
submitButton.pack()

window.mainloop()
