import traceback
import __future__
import sqlite3
import sys
# from openpyxl.utils import get_column_letter

from pyscraper.selenium_utils import get_headed_driver, wait_for_xpath, get_headless_driver
# from openpyxl import Workbook

driver = get_headless_driver(no_sandbox=True)
# for date in date_sequence('20170710', 10):
#     driver.get('http://www.kasi-time.com/day.php?date=' + date)

connection = sqlite3.connect('kasi.db')
cursor = connection.cursor()


errors = 0
start = int(sys.argv[1])
end = int(sys.argv[2])
try:
    for i in reversed(range(start)):
        if i == end: break
        try:
            driver.get('http://www.kasi-time.com/item-{}.html'.format(str(i)))
            TITLE =         driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/h1')[0].text.encode('utf-8')
            LYRICS =        driver.find_elements_by_xpath('//*[@id="lyrics"]')[0].text.encode('utf-8')
            singer =        driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td/a')[0].text.encode('utf-8')
            lyrics =        driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[2]/td/a')[0].text.encode('utf-8')
            composition =   driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[3]/td/a')[0].text.encode('utf-8')
            try: arrangement =   driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[4]/td/a')[0].text.encode('utf-8')
            except: traceback.print_exc(); arrangement = ''.encode('utf-8')
            try: category =      driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td/a')[0].text.encode('utf-8')
            except: traceback.print_exc(); category = ''.encode('utf-8')
            print(TITLE)
            
            cursor.execute("insert into lyrics values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(TITLE, LYRICS, singer, lyrics, composition, arrangement, category))
            connection.commit()
        except:
            traceback.print_exc()
            errors += 1

        print(i, errors)
finally:
    connection.close()
    #wb.save('kasi' + '.xlsx')

