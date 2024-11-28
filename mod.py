#!/usr/bin/python

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
	i = 0
	while i < 1000: 
		number = input("Enter number: ")
		intNumber = int(number)

		if intNumber in {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 15, 27, 30, 32, 34, 36}:	
			appendValue("rednumbers.txt", number)
			appendValue("blacknumbers.txt", " ")
			appendValue("greennumbers.txt", " ")
		if intNumber in {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}:
			appendValue("blacknumbers.txt", number)
			appendValue("greennumbers.txt", " ")
			appendValue("rednumbers.txt", " ")

		if intNumber in {0, 00}:
			appendValue("greennumbers.txt", number)
			appendValue("blacknumbers.txt", " ")
			appendValue("rednumbers.txt", " ")
		
		redLineCount = getLineCount("rednumbers.txt")
		if redLineCount > 10:
			delete_bot_line("rednumbers.txt")
			delete_bot_line("blacknumbers.txt")
			delete_bot_line("greennumbers.txt")
					

		i = i + 1

main()

