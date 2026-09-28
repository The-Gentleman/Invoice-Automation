import pdfplumber
from pprint import pprint
from pathlib import Path

invoice_path = Path(r"C:\Users\zraja\OneDrive - Signant Health\Documents\pythonstuff\caterer_invoice_INV-2026-0417.pdf")
#breakpoint()

with pdfplumber.open(invoice_path) as pdf:
   # get everything in "Description into a list"
    
    
   
