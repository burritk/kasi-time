from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import sqlite3

conn = sqlite3.connect('kasi.db')
c = conn.cursor()

wb  = Workbook()
ws = wb.active
for index, row in enumerate(c.execute('select * from lyrics')):
  for j, ro in enumerate(row):
    if j==0: print ro
    ws[get_column_letter(j+1) + str(index+1)] = ro
    
wb.save('test2.xlsx')
