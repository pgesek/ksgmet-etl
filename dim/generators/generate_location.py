#!/usr/bin/python
# coding=utf-8

from string import Template

print('id,x,y,europe')

hours_long = 7 * 24
hours_short = 48

line = Template('$id,$x,$y,$europe')

i = 1
for x_range, y_range, europe in zip([range(252), range(325)], [range(97), range(170)], [True, False]):
    for x in x_range:
        for y in y_range:
            values = dict(id = i, x = x, y = y, europe = europe)
            
            print(line.substitute(values))

            i += 1
