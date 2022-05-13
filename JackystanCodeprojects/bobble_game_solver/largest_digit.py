"""
File: largest_digit.py
Name: Jacky Chang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, number user entered. Be careful of minus sign compare only digits
	:return: int, the biggest digit in n, no care about minus sign
	"""
	# 數字的邊界條件
	max_dig = -float('inf')
	return find_largest_digit_helper(n, max_dig)
	# n = abs(n)
	# if n == 0:
	# 	return n
	# else:
	# 	return max(n % 10, find_largest_digit(n // 10))


def find_largest_digit_helper(n, max_dig):
		n = abs(n)
		if n == 0:
			return max_dig
		else:
			# 第一次recursion-->取數字n的個位數出來比較-->把n%10
			if n % 10 >= max_dig:
				max_dig = n % 10
				# 下一次recursion-->取數字n的十位數出來比較-->對數字(n//10)做function
				return find_largest_digit_helper(n//10, max_dig)
			else:
				# 下一次recursion-->取數字n的十位數出來比較-->對數字(n//10)做function
				return find_largest_digit_helper(n//10, max_dig)


if __name__ == '__main__':
	main()
