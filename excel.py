from openpyxl import Workbook
import sqlite3

conn = sqlite3.connect('kasi.db')
c = conn.cursor()

wb  = Workbook()
ws = wb.active
for row in c.execute('select * from lyrics'):
  for index, field in enumerate(row):
    ws['A' + str(index)] = field
  
wb.save('test.xlsx')
