from logging import root
import tkinter as tk 
import name2nucleotides as n2n
from name2nucleotides import name2protein, protein2dna, reverse_dna

# root = Tk()
# root.geometry('450x450')

# e = Entry(root, width = 100)
# e.pack()
# e.insert(0, 'Inserisci il tuo nome: ')
# #frame = Frame(root, height = 450, width = 450)
# #frame.pack()

# def myClick():
#     out = 'Il tuo nome in sequenza nucleotidica è: ' + e.get()
#     myLabel = Label(root, text = out)
#     myLabel.pack()

# myButton = Button(root, text = 'aaa', command = myClick)
# myButton.pack()

# def hide():
    

# myButton2 = Button(root, text = 'clear', command = hide)
# myButton2.pack()

# root.mainloop()

class Window:
    def __init__(self,master) -> None:
        self.master = root

        self.frame = tk.Frame(self.master, width = 450, height = 450)
        self.frame.pack()

        self.entry = tk.Entry(root, width = 100)
        self.entry.insert(0, '')
        self.entry.pack()
        self.entry.place(x = 50, y = 0)

        self.button = tk.Button(self.frame, text = 'Scopri la sequenza nucleotidica corrispondente', command = self.risultato)
        self.button.place(x = 50, y = 80)

        self.button2 = tk.Button(self.frame, text = 'clear', command = self.label_del)
        self.button2.place(x = 50, y = 120)
    
    def label_del(self):
        self.myLabel.destroy()

    def getname(self):
        self.entry.get()


    def risultato(self):
        #out2,out3=self.out()
        entry=name2protein(self.entry.get())
        out = 'Il tuo nome in sequenza nucleotidica è: ' + '\n' + str(protein2dna(entry))+'\n' + str(reverse_dna(protein2dna(entry)))
        # out = 'Il tuo nome in sequenza nucleotidica è: ' + '\n' + out2 + '\n' + out3
        self.myLabel = tk.Label(root, text = out)
        self.myLabel.pack()


if __name__=="__main__":
    root = tk.Tk()
    window = Window(root)
    name = window.getname()
    root.mainloop()
