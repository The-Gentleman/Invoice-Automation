import pdfplumber
from pprint import pprint
from pathlib import Path

invoice_path = Path(r"C:\Users\zraja\OneDrive - Signant Health\Documents\pythonstuff\caterer_invoice_INV-2026-0417.pdf")
#breakpoint()

with pdfplumber.open(invoice_path) as pdf:
     table = pdf.pages[0].extract_tables()
     food_items = []
    
     header = table[0][0]       
     item_code_column = header.index("Item Code")          
     desc_col = header.index("Description")
     qty_column = header.index("Qty")
     unit_column = header.index("Unit")
     unit_price_column = header.index("Unit Price")
     line_total_column = header.index("Line Total")
     #breakpoint()







     for element in table[0][1:]:
        food_items.append(element[1])

    

       
     

     
    
    
   
