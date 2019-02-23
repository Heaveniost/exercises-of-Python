# -*- coding: utf-8 -*- 
import re 

def get_filtered_words(file):
	with open(file, 'r') as f:
		data = f.read()
	words = re.findall(r'\w+', data)
	return words 

def output():	
	filtered_words = get_filtered_words(file)
	while True:
		tmp = input('input:')
		if tmp == '0':
			print('exit process success')
			break
		else:
			if tmp in filtered_words:
				print('output: Freedom')
			else:
				print('output: Human Rights')
	return 0

if __name__ == '__main__':
	file = './Docs/filtered_words.txt'
	print('enter 0 to exit process')
	output()
