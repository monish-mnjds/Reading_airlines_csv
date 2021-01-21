import xlrd
from collections import defaultdict
from pprint import pprint

l = []
wb = xlrd.open_workbook('E:/dataset/airlines.xls')
ws = wb.sheet_by_name("airlines")
rows = ws.get_rows()
next(rows)

for row in rows:
    l.append({'code':row[0].value, 'name':row[1].value, 'year':row[2].value, 'stats':row[3].value})

d = defaultdict(int)

for item in l:
    if item['name'] in d:
        d[item['name']] += 1
          
    if item['name'] not in d:
        d[item['name']] = 1

pprint(list(d.items()))

highest_ = sorted( d.items(), key = lambda item : item[-1])[-1]
print('\n\nAirport which is Mentioned the most number of times ----> ', highest_)

lowest_ = sorted( d.items(), key = lambda item : item[-1], reverse = True)[-1]
print('\n\nAirport which is Mentioned the least number of times ----> ', lowest_)
