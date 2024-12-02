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

class RouletteOdds:
	def __init__(self):
		self.odd   = 0
		self.even  = 0
		self.red   = 0
		self.black = 0
		self.low   = 0
		self.high  = 0
		self.total  = 0

	def increment(self):
		self.total = self.total + 1
	
	def decrement(self):
		self.total = self.total - 1

	def refresh(self):
		self.generate()
		delete_bot_line("odd.txt")
		delete_bot_line("even.txt")
		delete_bot_line("red.txt")
		delete_bot_line("zero.txt")
		delete_bot_line("black.txt")
		delete_bot_line("low.txt")
		delete_bot_line("high.txt")

		appendValue("odd.txt", self.odd_val)
		appendValue("even.txt", self.even_val)
		appendValue("red.txt", self.red_val)
		appendValue("black.txt", self.black_val)
		appendValue("zero.txt", self.zero_val)
		appendValue("low.txt", self.low_val)
		appendValue("high.txt", self.high_val)

	def generate(self):
		self.odd_val = str(int((self.odd / self.total) * 100))
		self.even_val = str(int((self.even / self.total) * 100))
		self.red_val = str(int((self.red / self.total) * 100))
		self.black_val = str(int((self.black / self.total) * 100))
		self.zero_val = str(int(((self.total - (self.red + self.black)) / self.total) * 100))
		self.high_val = str(int((self.high / self.total) * 100))
		self.low_val = str(int((self.low / self.total) * 100))

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
	
	odds = RouletteOdds()

	while True: 
		number = input("Enter number: ")
		
		if number == 'd':
			delete_top_line("rednumbers.txt")
			delete_top_line("blacknumbers.txt")	
			delete_top_line("greennumbers.txt")
			i -= 1
			odds.decrement()

			if lastVal == 0 or lastColor == "orange":
				continue
			if lastVal % 2 == 0:
				even -= 1
				odds.even = odds.even - 1
			else:
				odd -= 1
				odds.odd = odds.odd - 1
			if lastColor == "black":
				black -= 1;
				odds.black = odds.black - 1
			elif lastColor == "red":
				red -= 1;
				odds.red = odds.red - 1
			if lastVal > 18:
				high -= 1
				odds.high = odds.high - 1
			else:
				low -= 1
				odds.low = odds.low - 1
			
			odds.refresh()
			continue

		intNumber = int(number)

		if intNumber > 36:
			continue

		if intNumber % 2 == 0:
			if intNumber != 0 and intNumber != 00:
				even += 1;
				odds.even = odds.even + 1
		else:
			odd += 1
			odds.odd = odds.odd + 1

		if intNumber > 18 and intNumber < 37:
			high += 1;
			odds.high = odds.high + 1
		elif intNumber > 0:
			low += 1;
			odds.low = odds.low + 1

		if intNumber in {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23,25, 15, 27, 30, 32, 34, 36}:
			red += 1
			odds.red = odds.red + 1	
			lastColor = "red"
			appendValue("rednumbers.txt", number)
			appendValue("blacknumbers.txt", " ")
			appendValue("greennumbers.txt", " ")
		elif intNumber in {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}:
			black += 1
			odds.black = odds.black + 1
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
		odds.increment()
		lastVal = intNumber

		odds.refresh()

main()

