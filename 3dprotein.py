#from curses import window
#from logging import root
import cmd
import ssl
from unittest import result
import Bio
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
import csv
import sys
sys.path.append("/opt/homebrew/bin/pymol")
import pymol



def showStructurePyMOL(structura=None,pdb_id=None):
    '''
    Show structure using pymodule scripting
    '''
    cmd.fetch(pdb_id)
    cmd.spectrum()
    cmd.zoom()
    cmd.png('tmp/test.png', 1920, 1080)

pdb_id="7XQ3"
showStructurePyMOL(pdb_id)