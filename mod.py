#!/usr/bin/python

def delete_top_line(textFile):
	with open(textFile, "r") as file:
		lines = file.readlines()
	with open(textFile, "w") as file:
		file.writelines(lines[1:])


def delete_bot_line(textFile):
	with open(textFile, "r") as file:
		lines = file.readlines()
	with open(textFile, "w") as file:
		file.writelines(lines[:-1])


def getLineCount(textFile):
	with open(textFile, "r") as file:
		line_count = sum(1 for line in file)
	return line_count

def appendValue(textFile, value):
	with open(textFile, "r") as file:
		content = file.read()

	with open(textFile, "w") as file:
		file.write(value + "\n" + content)


def main():
	total = 0;
	red = 0;
	black = 0;
	even = 0;
	odd = 0;
	i = 0
	low = 0;
	high = 0;
	lastVal = 0;
	lastColor = "orange";
	while i < 1000: 
		number = input("Enter number: ")
		
		if number == 'd':
			delete_top_line("rednumbers.txt")
			delete_top_line("blacknumbers.txt")	
			delete_top_line("greennumbers.txt")
			i -= 1
			if lastVal == 0 or lastColor == "orange":
				continue
			if lastVal % 2 == 0:
				even -= 1
			else:
				odd -= 1
			if lastColor == "black":
				black -= 1;
			elif lastColor == "red":
				red -= 1;
			if lastVal > 18:
				high -= 1
			else:
				low -= 1
				
			continue

		intNumber = int(number)

		if intNumber > 36:
			continue

		if intNumber % 2 == 0:
			if intNumber != 0 and intNumber != 00:
				even += 1;
		else:
			odd += 1

		if intNumber > 18 and intNumber < 37:
			high += 1;
		elif intNumber > 0:
			low += 1;

		if intNumber in {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 15, 27, 30, 32, 34, 36}:
			red += 1	
			lastColor = "red"
			appendValue("rednumbers.txt", number)
			appendValue("blacknumbers.txt", " ")
			appendValue("greennumbers.txt", " ")
		elif intNumber in {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}:
			black += 1
			lastColor = "black"
			appendValue("blacknumbers.txt", number)
			appendValue("greennumbers.txt", " ")
			appendValue("rednumbers.txt", " ")
		elif intNumber in {0, 00}:
			appendValue("greennumbers.txt", number)
			appendValue("blacknumbers.txt", " ")
			appendValue("rednumbers.txt", " ")
		
		redLineCount = getLineCount("rednumbers.txt")
		if redLineCount > 10:
			delete_bot_line("rednumbers.txt")
			delete_bot_line("blacknumbers.txt")
			delete_bot_line("greennumbers.txt")
				
		i = i + 1
		lastVal = intNumber

		if getLineCount("odd.txt") > 0:
			delete_bot_line("odd.txt")
		if getLineCount("even.txt") > 0:
			delete_bot_line("even.txt")
		if getLineCount("red.txt") > 0:
			delete_bot_line("red.txt")
		if getLineCount("zero.txt") > 0:
			delete_bot_line("zero.txt")
		if getLineCount("black.txt") > 0:
			delete_bot_line("black.txt")
		if getLineCount("low.txt") > 0:
			delete_bot_line("low.txt")
		if getLineCount("high.txt") > 0:
			delete_bot_line("high.txt")

		odd_val = str(int((odd / i) * 100))
		even_val = str(int((even / i) * 100))
		red_val = str(int((red / i) * 100))
		black_val = str(int((black / i) * 100))
		zero_val = str(int(((i - (red + black)) / i) * 100))
		high_val = str(int((high / i) * 100))
		low_val = str(int((low / i) * 100))

		appendValue("odd.txt", odd_val)
		appendValue("even.txt", even_val)
		appendValue("red.txt", red_val)
		appendValue("black.txt", black_val)
		appendValue("zero.txt", zero_val)
		appendValue("low.txt", low_val)
		appendValue("high.txt", high_val)

main()

