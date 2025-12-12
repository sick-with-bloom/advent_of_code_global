from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")
	data = [line.split(": ") for line in data]
	data = [[line[0], line[1].split(" ")] for line in data]
	data = {line[0] : line[1] for line in data}
	return data



def part1(data):
	answer = 0
	start = "you"
	end = "out"
	paths = []

	queue = []

	return answer

def part2(data):
	answer = 0

	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(data)
print(part1(data))
print(part2(data))