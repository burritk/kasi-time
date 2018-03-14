from openpyxl import Workbook
import sqlite3

conn = sqlite3.connect('kasi.db')
c = conn.cursor()

wb  = Workbook()
ws = wb.active
for row in c.execute('select * from lyrics'):
  TITLE, LYRICS, singer, lyrics, composition, arrangement, category = row
  print TITLE
  ws['A' + str(1)] = TITLE
  ws['A' + str(2)] = LYRICS
  ws['A' + str(3)] = singer
  ws['A' + str(4)] = lyrics
  ws['A' + str(5)] = composition
  ws['A' + str(6)] = arrangement
  ws['A' + str(7)] = category
  
wb.save('test.xlsx')
