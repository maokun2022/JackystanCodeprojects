"""
File: boggle.py
Name: Jacky Chang
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This function search all anagrams of user type by 4 rolls letters in dictionary.txt
	"""
	####################
	s_lst = []
	s1 = input('1 row of letters: ')
	if form_check(s1):
		s1 = s1.lower()
		new_s1 = ''
		for ch in s1:
			if ch.isalpha():
				new_s1 += ch
		row1 = new_s1.split(',')
		s_lst += row1
		s2 = input('2 row of letters: ')
		if form_check(s2):
			s2 = s2.lower()
			new_s2 = ''
			for ch in s2:
				if ch.isalpha():
					new_s2 += ch
			row2 = new_s2.split(',')
			s_lst += row2
			s3 = input('3 row of letters: ')
			if form_check(s3):
				s3 = s3.lower()
				new_s3 = ''
				for ch in s3:
					if ch.isalpha():
						new_s3 += ch
				row3 = new_s3.split(',')
				s_lst += row3
				s4 = input('4 row of letters: ')
				if form_check(s4):
					s4 = s4.lower()
					new_s4 = ''
					for ch in s4:
						if ch.isalpha():
							new_s4 += ch
					row4 = new_s4.split(',')
					s_lst += row4
					start = time.time()
					find_anagrams(s_lst)
					end = time.time()
					print('----------------------------------')
					print(f'The speed of your boggle algorithm: {end - start} seconds.')
				else:
					print('Illegal input')
			else:
				print('Illegal input')
		else:
			print('Illegal input')
	else:
		print('Illegal input')
	####################
	# s_lst = [ 'fycl', 'iomg', 'oril', 'hjhu']


def form_check(s):
	# s1-s4 should be "alpha -> ' ' -> alpha -> ' ' -> alpha -> ' ' -> alpha"
	# index              0       1       2       3       4       5       6
	if len(s) != 7:
		return False
	else:
		for i in range(len(s)):
			ch = s[i]
			if i % 2 == 0 and ch.isalpha():
				pass
			elif i % 2 == 1 and ch == ' ':
				pass
			else:
				return False
		return True


def find_anagrams(s_lst):
	"""
	:param s_lst: dict, user type to search anagrams
	:return: print all anagrams and count the number of anagrams
	"""
	word_lst = read_dictionary(s_lst)
	answer_lst = []
	for x in range(4):
		for y in range(4):
			coordinates = [(x, y)]
			current_s = s_lst[x][y]
			find_anagrams_helper(s_lst, current_s, x, y, coordinates, answer_lst, word_lst)
	print('There are', (len(answer_lst)), 'words in total.')


def find_anagrams_helper(s_lst, current_s, x, y, coordinates, answer_lst, word_lst):
	"""
	:param s_lst: list, user type to search anagrams. contain 4 list with rows of letters
	:param current_s: str, empty str for anagram searching
	:param x: int, to save x index for now-searching letter on 4*4 board
	:param y: int, to save y index for now-searching letter on 4*4 board
	:param coordinates: list, to save coordinates for word now-searching
	:param answer_lst: list, to save answer anagrams
	:param word_lst: list, consistent with all word len >= 4 and word[0] contains in s_lst
	"""
	if len(current_s) >= 4:
		if current_s not in answer_lst:
			if current_s in word_lst:
				print('Found: ' + current_s)
				answer_lst.append(current_s)

	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			if 0 <= i <= 3 and 0 <= j <= 3:
				if (i, j) not in coordinates:
					# Choose
					current_s += s_lst[i][j]
					coordinates.append((i, j))
					if has_prefix(current_s, word_lst):
						# explore
						find_anagrams_helper(s_lst, current_s, i, j, coordinates, answer_lst, word_lst)
					# Un_choose
					coordinates.pop()
					current_s = current_s[:-1]


def read_dictionary(s_lst):
	word_lst = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			for ch in s_lst:
				if len(word) >= 4 and word[0] in ch:
					# 依題意只須找長度 >=4且字首有包含任一個輸入字母的字
					word_lst.append(word)
	return word_lst


def has_prefix(sub_s, word_lst):
	"""
	:param sub_s: str, consistent with any alphabet combinations from 's' user type
	:param word_lst: list, consistent with all word len >= 4 and word[0] contains in s_lst
	:return: boolean, check if word in word_lst start with sub_s
	"""
	for word in word_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
