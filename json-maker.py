import sqlite3
import json
import os
import sys

conn = sqlite3.connect('kasi.db')
c = conn.cursor()
songs = []
limit = 100000

try: limit = int(sys.argv[1])
except: pass

counter = 0
for row in c.execute('select * from lyrics'):
  counter += 1
  if counter == limit: break
  
  song = {
    'title': row[0].encode('utf-8'),
    'lyrics': row[1].encode('utf-8'),
    'singer': row[2].encode('utf-8'),
    'author': row[3].encode('utf-8'),
    'composition': row[4].encode('utf-8'),
    'arrangement': row[5].encode('utf-8'),
    'category': row[6].encode('utf-8')
  }
  songs.append(song)

try:
  os.remove('lyrics.json')
except:
  pass

with open('lyrics.json', 'a+') as output:
  output.write(json.dumps({'songs': songs}))
  
print 'done'
