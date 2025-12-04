from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")
	data = [line.split("   ") for line in data]
	return data

directions = {"L":-1,"R":1}

def part1(data):
	answer = 0
	left = sorted([int(line[0]) for line in data])
	right = sorted([int(line[1]) for line in data])
	for i in range(len(data)):
		answer += abs(left[i] - right[i])
	return answer

def part2(data):
	answer = 0
	left = [int(line[0]) for line in data]
	right = [int(line[1]) for line in data]
	for i in range(len(data)):
		answer += left[i] * right.count(left[i])
	return answer

data = read_data(__file__, "2024")
data = handle(data)
print(part1(data))
print(part2(data))