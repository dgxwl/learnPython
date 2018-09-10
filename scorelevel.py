#!/usr/bin/env python3
# -*- coding: utf-8 -*-

g = input('Input your grade: ')
g = int(g)

if g < 0 or g > 100:
	print('Invalid grade.')
else:
	if g >= 80:
		print('Excellent!')
	elif g >= 70:
		print('Great.')
	elif g >= 60:
		print('Passed.')
	else:
		print('Failed.')