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
        try:
            if i == end: break
            try:
                driver.get('http://www.kasi-time.com/item-{}.html'.format(str(i)))
                TITLE =         driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/h1')[0].text
                LYRICS =        driver.find_elements_by_xpath('//*[@id="lyrics"]')[0].text
                singer =        driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td/a')[0].text
                lyrics =        driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[2]/td/a')[0].text
                composition =   driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[3]/td/a')[0].text
                try: arrangement =   driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[4]/td/a')[0].text
                except: arrangement = ''
                try: category =      driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td/a')[0].text
                except: category = ''
                print(TITLE)
                query = "insert into lyrics values(?, ?, ?, ?, ?, ?, ?)"
                #print query
                cursor.execute(query, (TITLE, LYRICS, singer, lyrics, composition, arrangement, category))
                connection.commit()
            except:
                traceback.print_exc()
                errors += 1
        except:
            driver = get_headless_driver(no_sandbox=True)
            print 'going headless'
            continue
        print(i, errors)
finally:
    connection.close()
    #wb.save('kasi' + '.xlsx')

