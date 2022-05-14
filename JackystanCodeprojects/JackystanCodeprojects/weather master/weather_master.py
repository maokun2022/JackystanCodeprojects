"""
File: weather_master.py
Name: Jacky Chang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	This weather master will calculate the highest, lowest, average temperatures of data User entered. Also
	count the number of days below -16 degrees.
	"""
	print('stanCode \"Weather master 4.0\"!')
	x = int(input('Next Temperature:' + ' (or ' + str(EXIT) + ' to quit)? '))
	if x == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = x
		maximum != EXIT
		# Do not count EXIT when picking highest temperature
		minimum = x
		minimum != EXIT
		# Do not count EXIT when picking lowest temperature
		a = 0
		# It counts number of cold days
		b = 0
		# It counts number of entered temperature(s)
		c = 0
		# It counts sum of entered temperature(s)
		while True:
			if x == EXIT:
				break
			if x >= maximum:
				maximum = x
			if x <= minimum:
				minimum = x
			if x < 16:
				a = a + 1
			b = b + 1
			c = c + x
			x = int(input('Next Temperature:' + ' (or ' + str(EXIT) + ' to quit)? '))
		average = float(c / b)
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(a) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
