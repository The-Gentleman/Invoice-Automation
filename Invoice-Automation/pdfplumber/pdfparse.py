import pdfplumber
from pprint import pprint
from pathlib import Path

invoice_path = Path(r"C:\Users\zraja\OneDrive - Signant Health\Documents\pythonstuff\caterer_invoice_INV-2026-0417.pdf")
#breakpoint()

with pdfplumber.open(invoice_path) as pdf:
     table = pdf.pages[0].extract_tables()
     food_items = []
     quantities = []
     header = table[0][0]                 
     desc_col = header.index("Description")
     breakpoint()
     for element in table[0][1:]:
        food_items.append(element[1])

    

       
     

     
    
    
   
