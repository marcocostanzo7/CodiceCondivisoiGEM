#from curses import window
#from logging import root
import ssl
from unittest import result
import Bio
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW

sequence = "GGCATCAACAGAGGCATCCTGGACCTGAACGGCGAGCTGAAC"

ssl._create_default_https_context = ssl._create_unverified_context
result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)
            print(hsp. match)
            print(hsp.sbjct)