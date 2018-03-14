from openpyxl import Workbook
import sqlite3

conn = sqlite3.connect('kasi.db')
c = conn.cursor()

wb  = Workbook()
ws = wb.active
for index, row in enumerate(c.execute('select * from lyrics')):
  print row
  ws['A' + str(index)] = row
  
wb.save('test.xlsx')