#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from tkinter import *
from tkinter import ttk
import amem, log, terms

class Window(Frame):

    def __init__(self, parent):

        self.master = parent
        self.master.bind('<Return>', self.input)
        
        Frame.__init__(self, parent)
        Frame.config(self, bg = "pink")

        self.prompt = Label(self, text = "Insira uma frase em japonês:", bg = "pink", font = ('Lucinda Grande','15'))
        self.entry = Entry(self, bd = 0)
        self.detail_button = Button(self, text = "Detalhar", command = self.input, highlightbackground = "pink")

        self.translation_label = Label(self, text = "Tradução:", bg = "pink", font = ('Lucinda Grande','15'))
        self.translation_text = Text(self, height = 1, width = 49)

        self.explanation_label = Label(self, text = "Explicação:", bg = "pink", font = ('Lucinda Grande','15'))
        self.explanation_text = Text(self, height = 23, width = 49)

        self.treeview = ttk.Treeview(self)
        self.treeview.bind("<Double-Button-1>", self.tree_click)

        # Gridding
        
        self.prompt.grid(row = 0, column = 0, columnspan = 3, padx = 10, sticky = W)
        self.entry.grid(row = 1, column = 0, columnspan = 3, padx = 10, ipadx = 80, sticky = W)
        self.detail_button.grid(row = 1, column = 4, padx = 10)

        self.translation_label.grid(row = 2, column = 0, columnspan = 3, padx = 10, sticky = W)
        self.translation_text.grid(row = 3, column = 0, columnspan = 3, padx = 10, sticky = NW)

        self.explanation_label.grid(row = 4, column = 0, columnspan = 3, padx = 10, sticky = W)
        self.explanation_text.grid(row = 5, column = 0, columnspan = 3, padx = 10, pady = 10)

        self.treeview.grid(row = 2, column = 4, rowspan = 4, padx = 10, ipady = 70)

    def tree_click(self,event):
        
        self.explanation_text.delete(1.0,END)

        node = self.treeview.focus()

        print(self.info_dict)
        print(self.item_dict)

        if node != '' and node in self.item_dict:
            token = self.info_dict[self.item_dict[node]]
            if token == 'VERB' and log.verb == 'MASU' :
                self.explanation_text.insert(END,terms.info[token] + "\n" + terms.info['MASU'])
            else :
                self.explanation_text.insert(END,terms.info[token])
            

    def input(self,event = None):
        
        log.reset()

        self.treeview.delete(*self.treeview.get_children())
        self.explanation_text.delete(1.0,END)
        self.translation_text.delete(1.0,END)
        
        text = self.entry.get()

        translated = amem.main(text)

        if log.error != "" :

            self.explanation_text.insert(END,log.error)
            log.clear_error()
            
        else :

            self.set_treeview(self)
            self.translation_text.insert(END,translated)


    def set_treeview(self,event):

        words = log.phrase
        tokens = log.explain

        print(words)
        print(tokens)

        self.info_dict = dict(zip(words,tokens))
        self.item_dict = {}

        self.treeview.insert('','0','sentenca',text = "Sentença")

        item_count = 0
        item_name = 'item' + str(item_count)

        if log.has_topic :
            self.treeview.insert('sentenca','end','topico',text = "Tópico")
            self.treeview.insert('topico','end','nominal',text = "S. Nominal")
            while (words[item_count] != "は"):
                item_name = 'item' + str(item_count)
                self.treeview.insert('nominal','end',item_name,text = words[item_count])
                self.item_dict[item_name] = words[item_count]
                item_count = item_count + 1
            item_name = 'item' + str(item_count)
            self.treeview.insert('topico','end',item_name,text = "は")
            self.item_dict[item_name] = words[item_count]
            item_count = item_count + 1
        
        if (log.sentence_type == 'VERBAL'):
            self.treeview.insert('sentenca','end','info',text = "Informação")
            nom_count = 0
            while (self.info_dict[words[item_count]] != 'VERB' and self.info_dict[words[item_count]] != 'AUX_VERB'):
                self.treeview.insert('info','end','nominal_info' + str(nom_count),text = "S. Nominal")
                while self.info_dict[words[item_count]] not in terms.particles:
                    item_name = 'item' + str(item_count)
                    self.treeview.insert('nominal_info' + str(nom_count),'end',item_name,text = words[item_count])
                    self.item_dict[item_name] = words[item_count]
                    item_count = item_count + 1
                item_name = 'item' + str(item_count)
                self.treeview.insert('info','end',item_name,text = words[item_count]) # Particle
                self.item_dict[item_name] = words[item_count]
                item_count = item_count + 1
                print(self.info_dict[words[item_count]])
                nom_count = nom_count + 1
        elif (log.sentence_type == 'DESCRIPTIVE'):
            self.treeview.insert('sentenca','end','info',text = "Informação")
            self.treeview.insert('info','end','nominal_info',text = "S. Nominal")
            while self.info_dict[words[item_count]] != 'AUX_VERB':
                item_name = 'item' + str(item_count)
                self.treeview.insert('nominal_info','end',item_name,text = words[item_count])
                self.item_dict[item_name] = words[item_count]
                item_count = item_count + 1

        if (self.info_dict[words[item_count]] == 'VERB'):
            self.treeview.insert('sentenca','end','verb_label',text = "Verbo")
            self.treeview.insert('verb_label','end','verb',text = words[item_count])
            self.item_dict['verb'] = words[item_count]
            item_count = item_count + 1
        elif (self.info_dict[words[item_count]] == 'AUX_VERB'):
            self.treeview.insert('sentenca','end','copula_label',text = "Cópula")
            self.treeview.insert('copula_label','end','copula',text = words[item_count])
            self.item_dict['copula'] = words[item_count]
            item_count = item_count + 1

        if log.question : 
            self.treeview.insert('sentenca','end','ka',text = 'か')
            self.item_dict['ka'] = words[item_count]
            item_count = item_count + 1


root = Tk()
root.title("DESU by Glamour")
root.geometry('600x520')
root.resizable(0,0)

w = Window(root)
w.grid_propagate(False)

w.pack(fill = "both", expand = True)
w.columnconfigure(0, weight = 1)
w.columnconfigure(1, weight = 1)
w.columnconfigure(2, weight = 1)
w.columnconfigure(3, weight = 1)
w.columnconfigure(4, weight = 1)
w.columnconfigure(5, weight = 1)
w.columnconfigure(6, weight = 1)

root.mainloop()





