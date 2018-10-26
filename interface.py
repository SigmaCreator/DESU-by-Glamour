from tkinter import *
import amem

class Window(Frame):

    def __init__(self, parent):

        self.master = parent

        Frame.__init__(self, parent)
        Frame.config(self, bg = "pink")

        self.prompt = Label(self, text = "Coloque uma frase em japonês: ", justify = CENTER, bg = "pink")
        self.entry = Entry(self)
        self.translate = Button(self, text = "Traduzir", command = self.input, bg = "pink")

        self.prompt.pack(side = "top", fill = "x")
        self.entry.pack(side = "top", fill = "x", padx = 20)
        self.translate.pack()

    def input(self):
        
        text = self.entry.get()
        amem.main(text)

root = Tk()

w = Window(root)

Window(root).pack(fill = "both", expand = True)

root.mainloop()





