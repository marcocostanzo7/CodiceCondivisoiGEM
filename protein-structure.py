import logging as log
from this import s
from Bio.Blast import NCBIWWW
from Bio.PDB import PDBParser, PDBList
from Bio.PDB.MMCIF2Dict import MMCIF2Dict
from Bio.PDB.mmcifio import MMCIFIO
from Bio.PDB.PDBIO import PDBIO
from Bio.PDB.MMCIFParser import MMCIFParser
import cmd

protein = "1FAT"

# #reading a mmCIF file
# def mmCIF_reader():
#     parser = MMCIFParser()
#     structure = parser.get_structure("protein_id", "protein_id.cif")
#     mmcif_dict = MMCIF2Dict("protein_id.cif") #create a Python dictionary that maps all mmCIF tags in an mmCIF file to their values
#     return(structure)

# #reading a PDB file
# def PDB_reader():
#     parser = PDBParser(PERMISSIVE=1)
#     structure_id = "protein_id"
#     filename = "protein_id.ent"
#     structure = parser.get_structure(structure_id, filename)
#     name = structure.name["mame"]
#     head = structure.head["head"]
#     return(name, head)

# #writing a mmCIF file
# def mmCIF_writer():
#     io = MMCIFIO()
#     io.set_structure(s)
#     io.save("out.cif")

# #writing a PDF file
# def PDB_writer():
#     io = PDBIO()
#     io.set_structure(s)
#     io.save("out.pdb")



#downloading PDB file
def _downloadpdbfile(pdb_id:str):
    pdblist_manager=PDBList()
    log.debug("downloadpdbfiles: downloading")
    pdblist_manager.retrieve_pdb_file(pdb=[pdb_id])

#printing protein structure
def protein_structure(pdb_id:str):
    _downloadpdbfile(pdb_id)
    parser=PDBParser()
    return parser.get_structure(pdb_id,f"{pdb_id}.pdb")

# show structure with PyMOL
def show_structure(structura=None, pdb_id=None):
    cmd.fetch(pdb_id)
    cmd.spectrum()
    cmd.zoom()
    cmd.png('tmp/test.png', 1920, 1080)

show_structure(protein)



