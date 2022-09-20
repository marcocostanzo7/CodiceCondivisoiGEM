#from curses import window
#from logging import root
import re
from Bio.Seq import Seq
import tkinter as tk 
#from CodeWithGraphic import Window


amm=[ 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

#window = Window()
#name = window.getname()

def _replace(ch:str)->str:
    ''' 
    Utility function for replacing not aminoacids characters
        Param:
            ch| character in input
        Return:
            a| new character
    '''
    if ch in amm:
        return ch
    else:
        a=list(sorted(amm, key=lambda x:abs(ord(ch.upper())-ord(x))))[0]
        return a

def name2protein(name:str)->str:
    '''
    Function for converting name 2 polypeptide sequence
    
    Input:
        name| input name
    Return:
        sequence| motif
    '''
    name=re.sub(r'\W+', '', name)
    newname=list(map(_replace, [*name]))
    newname="".join(newname)
    return newname

def protein2dna(protein:str):
    dna = ''
    codon_table = {
        'A':'CTG',
        'C':'TGC',
        'D':'GAC',
        'E':'GAG',
        'F':'TTC',
        'G':'GGC',
        'H':'CAC',
        'I':'ATC',
        'K':'AAG',
        'L':'CTG',
        'M':'ATG',
        'N':'AAC',
        'P':'CCC',
        'Q':'CAG',
        'R':'AGA',
        'S':'AGC',
        'T':'ACC',
        'V':'GTG',
        'W':'TGG',
        'Y':'TAC'  
        }
    for i in protein:
        conversion = codon_table[i]
        dna = dna+conversion
    return(dna)

def reverse_dna(final:str):
    my_seq = Seq(final)
    complement_dna = my_seq.complement()
    return(complement_dna)

if __name__=="__main__":
    pass
    # root = tk.Tk()
    # window = Window(root)
    # name = window.getname()
    # root.mainloop()



    # output1 = name2protein(name)
    # output2 = protein2dna(output1)
    # output3 = str(reverse_dna(output2))
    # output2 = str(output2)
