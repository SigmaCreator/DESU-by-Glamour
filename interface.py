from tkinter import *
import amem
import pygame

class Window(Frame):

    def __init__(self, parent):

        pygame.mixer.init()
        pygame.mixer.music.load('death-by-glamour.mp3')
        pygame.mixer.music.play()

        self.master = parent
        self.master.bind('<Return>', self.input)
        
        Frame.__init__(self, parent)
        Frame.config(self, bg = "pink")

        self.prompt = Label(self, text = "Coloque uma frase em japonês: ", bg = "pink")
        self.entry = Entry(self)
        self.translate = Button(self, text = "ってゆうか", command = self.input, bg = "pink")

        self.explanation = Label(self, text = "Explicação")
        self.translation = Label(self, text = "Tradução")

        self.prompt.grid(row = 0, column = 0)
        self.entry.grid(row = 0, column = 1)
        self.translate.grid(row = 0, column = 2, padx = 10)
        self.translation.grid(row = 1, column = 0, ipadx = 50, ipady = 50)
        self.explanation.grid(row = 1, column = 1, ipadx = 50, ipady = 50)
        
  

    def input(self, event = None):
        
        text = self.entry.get()
        amem.main(text)

root = Tk()

w = Window(root)

Window(root).pack(fill = "both", expand = True)
root.title("Glamour - Japanese Tool")
root.mainloop()





