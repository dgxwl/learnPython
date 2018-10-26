#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def generate():
	chs = ''
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	while True:
		l = letters[random.randint(0, len(letters)-1)]
		if chs.find(l) != -1:
			continue
		chs += l
		if len(chs) == 5:
			return chs

def check(answer, guess):
	result = [0, 0]
	for i in range(len(answer)):
		for j in range(len(guess)):
			if answer[i] == guess[j]:
				result[0] += 1
				if i == j:
					result[1] += 1
	return result

print('猜字符游戏. 输入EXIT退出')
answer = generate()
print(answer) #cheat
wrongCount = 0
while True:
	if wrongCount < 10:
		guess = input('猜吧: ').upper()
		if guess == 'EXIT':
			print('再见')
			break
		result = check(answer, guess)
		if result[1] == len(answer):
			print('猜对了!总分: %d' % (100 - wrongCount * 10))
			break
		else:
			wrongCount += 1
			print('猜对了%d个字符, 其中位置对了%d个' % (result[0], result[1]))
	else:
		print('游戏结束, 得分: 0')
		break
	
