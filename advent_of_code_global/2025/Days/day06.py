from math import prod
from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")
	data = [line.split(" ") for line in data]
	data = [[_ for _ in line if _ != ""] for line in data]
	data = [[int(_) if _.isdigit() else _ for _ in line ] for line in data]
	return data

def part1(data):
	answer = 0
	for i in range(len(data[0])):
		line = [_[i] for _ in data]
		operator = line[-1]
		subAnswer = line[0]
		for operand in line[1:-1]:
			if operator == "*":
				subAnswer *= operand
			elif operator == "+":
				subAnswer += operand
		answer += subAnswer

	return answer

def part2(data):
	answer = 0
	data = read_data(__file__, "2025").split("\n")
	operators = data[-1]
	operands = data[:-1]
	columnBreaks = []

	for i in range(len(operators)):
		if operators[i] != " ":
			columnBreaks.append(i)

	operators = list(_ for _ in operators if _ in ["+","*"])
	realData = [[] for _ in operands]

	for i in range(len(realData)):
		row = operands[i]
		for c in range(len(columnBreaks) - 1):
			part = row[columnBreaks[c]:columnBreaks[c+1]-1]
			start = columnBreaks[c]
			end = columnBreaks[c+1]
			realData[i].append(part)
		lastPart = row[columnBreaks[-1]:]
		realData[i].append(lastPart)

	cols = [[] for _ in range(len(realData[i]))]

	for i in range(len(cols)):
		for r in range(len(realData)):
			cols[i].append(realData[r][i])
		cols[i].append(operators[i])

	cols = [[list(num) for num in line] for line in cols]
	cols = [[thing[::-1] for thing in line[::-1]] for line in cols[::-1]]

	for line in cols:
		numbers = line[1:]
		operator = line[0][0]
		nums = []
		for i in range(len(numbers[0])):
			num = ""
			for j in range(len(numbers)-1,-1,-1):
				num += numbers[j][i]
			nums.append(int(num))
		if operator == "+":
			subAnswer = sum(nums)
		else:
			subAnswer = prod(nums)
		#print(operator.join([str(num) for num in nums]),"=",subAnswer)
		answer += subAnswer

	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(part1(data))
print(part2(data))