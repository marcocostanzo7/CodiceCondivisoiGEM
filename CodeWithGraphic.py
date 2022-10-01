from logging import root
import tkinter as tk
from tkinter.ttk import Style 
import name2nucleotides as n2n
from name2nucleotides import name2protein, protein2dna, reverse_dna, nameamm

class Window:
    def __init__(self,master) -> None:
        self.master = root

        self.frame = tk.Frame(self.master, width = 850, height = 550)
        self.frame.pack()

        self.entry = tk.Entry(root, width = 100)
        self.entry.insert(0, '')
        self.entry.pack()
        self.entry.place(x = 250, y = 200)

        self.button = tk.Button(self.frame, text = 'Scopri la sequenza nucleotidica corrispondente', command = self.risultato)
        self.button.place(x = 200, y = 280)

        self.button2 = tk.Button(self.frame, text = 'clear', command = self.label_del)
        self.button2.place(x = 200, y = 320)
    
    def label_del(self):
        self.myLabel.destroy()

    def getname(self):
        self.entry.get()


    def risultato(self):
        #out2,out3=self.out()
        entry=name2protein(self.entry.get())
        out1 = 'Il tuo nome in sequenza amminoacidica è: ' + '\n' + str(nameamm(entry)) + '\n'
        out2 = 'Il tuo nome in sequenza nucleotidica è: ' + '\n' + str(protein2dna(entry)) +'\n' + str(reverse_dna(protein2dna(entry)))
        try:
            self.myLabel.destroy()
        except:
            pass
        self.myLabel = tk.Label(root,text= out1 + out2)
        self.myLabel.pack()


if __name__=="__main__":
    root = tk.Tk()
    window = Window(root)
    name = window.getname()
    root.mainloop()
