import re
from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")

	return data

def part1(data):
	answer = 0
	for line in data:
		x = re.findall("mul\(", line)
		print(x)
	return answer

def part2(data):
	answer = 0
			
	return answer

data = read_data(__file__, "2024")
data = handle(data)
print(part1(data))
print(part2(data))