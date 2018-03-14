from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import sqlite3

conn = sqlite3.connect('kasi.db')
c = conn.cursor()

wb  = Workbook()
ws = wb.active
for index, row in enumerate(c.execute('select * from lyrics')):
  TITLE, LYRICS, singer, lyrics, composition, arrangement, category = row
  print TITLE
  ws[get_column_letter(index) + str(1)] = TITLE
  ws[get_column_letter(index) + str(2)] = LYRICS
  ws[get_column_letter(index) + str(3)] = singer
  ws[get_column_letter(index) + str(4)] = lyrics
  ws[get_column_letter(index) + str(5)] = composition
  ws[get_column_letter(index) + str(6)] = arrangement
  ws[get_column_letter(index) + str(7)] = category
  
wb.save('test2.xlsx')
