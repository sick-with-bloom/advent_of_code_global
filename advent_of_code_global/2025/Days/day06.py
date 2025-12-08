from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")
	data = [line.split(" ") for line in data]
	data = [[_ for _ in line if _ != ""] for line in data]
	data = [[int(_) if _.isdigit() else _ for _ in line ] for line in data]
	print(data)
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
			#print(operand,subAnswer)
		answer += subAnswer
			
		#print(line,subAnswer)

	return answer

def part2(data):
	answer = 0
	data = read_data(__file__, "2025").split("\n")
	operators = data[-1]
	columnBreaks = []
	for i in range(len(operators)):
		if operators[i] != " ":
			columnBreaks.append(i)

	realData = [[],[],[]]
	for i in range(len(columnBreaks) - 1):
		realData[0].append(data[0][columnBreaks[i]:columnBreaks[i+1]-1])
		realData[1].append(data[1][columnBreaks[i]:columnBreaks[i+1]-1])
		realData[2].append(data[2][columnBreaks[i]:columnBreaks[i+1]-1])


	print(columnBreaks)
	for row in realData:
		print(row)

	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(part1(data))
print(part2(data))