#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c)
	delta = b * b - 4 * a * c
	
	if delta > 0:
		return (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a, (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
	elif delta == 0:
		return (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
	else:
		return '无解'