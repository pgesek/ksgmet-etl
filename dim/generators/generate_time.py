#!/usr/bin/python
# coding=utf-8
from string import Template

print('id,hour,minute')

# we are starting at 1
steps = (24 * 60) + 1

minute = 0
hour = 0

line = Template('$id,$hour,$minute')

for i in range(1, steps):
    values = dict(id = i, minute = minute, hour = hour)
    print(line.substitute(values))

    minute += 1

    if minute % 60 == 0:
        hour += 1
        minute = 0
