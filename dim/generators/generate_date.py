#!/usr/bin/python
# coding=utf-8

from string import Template
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

print('id,date,year,month,day')

start_date = date(2018, 9, 1)
end_date = date(2019, 9, 1)

line = Template('$id,$date,$year,$month,$day')

i = 1
for date in daterange(start_date, end_date):
    values = dict(date = date, year = date.year, month = date.month, day = date.day, id = i)
    
    print(line.substitute(values))

    i += 1
