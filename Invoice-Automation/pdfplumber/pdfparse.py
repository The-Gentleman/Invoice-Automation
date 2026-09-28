import pdfplumber
import pandas as pd
from pprint import pprint
from pathlib import Path


invoice_path = Path(r"C:\Users\zraja\OneDrive - Signant Health\Documents\pythonstuff\caterer_invoice_INV-2026-0417.pdf")


with pdfplumber.open(invoice_path) as pdf:
     table = pdf.pages[0].extract_tables()[0]
#breakpoint()
invoice = pd.DataFrame(table[1:], columns= table[0]) # this grabs table from pdfplumber and manifests the data exactly like a spreadsheet. The column part adds the column names instead of just indexes
invoice.to_excel("invoice.xlsx", index=False) #.to_excel() writes the DataFrame to an Excel file. The first argument is the filename or full path, and index=False leaves out pandas' own row-number column.
#breakpoint()
     
    

   
    

       
     

     
    
    
   
