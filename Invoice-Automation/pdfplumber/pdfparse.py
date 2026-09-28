import pdfplumber
from pprint import pprint
from pathlib import Path

invoice_path = Path(r"C:\Users\zraja\OneDrive - Signant Health\Documents\pythonstuff\caterer_invoice_INV-2026-0417.pdf")
#breakpoint()

with pdfplumber.open(invoice_path) as pdf:
     table = pdf.pages[0].extract_tables()[0]
     food_items = []
    

   
    

       
     

     
    
    
   
