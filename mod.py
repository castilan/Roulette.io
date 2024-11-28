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
		color = input("Choose color(r, b, g): ")
		number = input("Enter number: ")
	
		if color == 'r':
			appendValue("rednumbers.txt", number)
			appendValue("blacknumbers.txt", " ")
			appendValue("greennumbers.txt", " ")

		if color == 'b':
			appendValue("blacknumbers.txt", number)
			appendValue("greennumbers.txt", " ")
			appendValue("rednumbers.txt", " ")


		elif color == 'g':
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

