#!/usr/bin/python
# coding=utf-8

from string import Template

print('id,is_long,hours_ahead')

hours_long = 7 * 24
hours_short = 48

line = Template('$id,$is_long,$hours_ahead')

i = 1
for (is_long, hour_range) in zip([True, False], [range(hours_long), range(hours_short)]):
    for hour in hour_range:
        values = dict(id = i, is_long = is_long, hours_ahead = hour)
        
        print(line.substitute(values))

        i += 1

