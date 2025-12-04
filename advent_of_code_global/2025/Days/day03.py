from utils.datahandler import read_data
import itertools

def handle(data):
	data = data.split("\n")
	return data

def solve(data, length = 12):
	answer = 0
	for line in data:
		c = 0
		num = ""
		while len(num) != length:
			highest = 0
			highestNum = "0"
			charsLeft = length - len(num)
			for i in range(c,len(line)-charsLeft+1):
				if line[i] > highestNum:
					highest = i
					highestNum = line[i]
			num += highestNum
			c = highest + 1
		answer += int(num)
	return answer

def day01(data):
	return solve(data,2)

def day02(data):
	return solve(data,12)


data = read_data(__file__, "2025")
data = handle(data)
print(day01(data))
print(day02(data))