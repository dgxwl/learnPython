#!/usr/bin/env python3
# -*- coding: utf-8 -*-

year = int(input('输入一个年份: '))

flag = (year%100!=0 and year%4==0) or year%400==0

if flag:
	print('Yes, it\'s a leap year.')
else:
	print('No, it isn\'t.')