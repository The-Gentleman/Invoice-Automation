import pdfplumber
from pprint import pprint
from pathlib import Path

invoice_path = Path(r"C:\Users\zraja\OneDrive - Signant Health\Documents\pythonstuff\caterer_invoice_INV-2026-0417.pdf")
#breakpoint()

with pdfplumber.open(invoice_path) as pdf:
     description_column_header = ""
     food_items = []
     
     table = pdf.pages[0].extract_tables()
     description_column_header = table[0][0][1]
     
     
     for element in table[0][1:]:
        food_items.append(element[1])

       
     #table gets everything into a nested list
     #table[0][0] gets the column headers
     print(food_items)

     
    
    
   
