from openpyxl import Workbook
import sqlite3

conn = sqlite.connect('kasi.db')
c = conn.cursor()

wb  = Workbook()
ws = wb.active
for index, row in enumerate(c.execute('select * from lyrics')):
  ws['A' + str(index)] = row
  
wb.save('test.xlsx')
