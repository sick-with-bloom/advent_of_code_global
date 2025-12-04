from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")
	data = [line.split(" ") for line in data]
	data = [[int(num) for num in line] for line in data]
	return data

def isSafe(line):
	increases = 0
	decreases = 0
	for i in range(len(line) - 1):
		if line[i] < line[i+1]:
			increases += 1
		if line[i] > line[i+1]:
			decreases += 1
		diff = abs(line[i] - line[i+1])
		if diff < 1 or diff > 3:
			return False
	if increases != 0 and decreases != 0:
		return False
	return True

def part1(data):
	answer = 0
	for line in data:
		if isSafe(line):
			answer += 1
	return answer

def part2(data):
	answer = 0
	for line in data:
		safes = 0
		for i in range(len(data)):
			cutLine = line[:i]
			cutLine.extend(line[i+1:])
			if isSafe(cutLine):
				safes += 1
		if safes != 0:
			answer += 1
			
	return answer

data = read_data(__file__, "2024")
data = handle(data)
print(part1(data))
print(part2(data))