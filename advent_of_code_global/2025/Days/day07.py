from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")
	data = [list(line) for line in data]
	return data

def display(data):
	for row in data:
		print("".join(row))
	print("~"*len(data[0]))

def same(data, buffer):
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] != buffer[i][j]:
				return False
	return True


def part1(data):
	answer = 0
	splits = {}
	buffer = [[_ for _ in row] for row in data]
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] == "S":
				buffer[i+1][j] = "|"
	while not same(data,buffer):
		data = [[_ for _ in row] for row in buffer]
		for i in range(len(data)):
			for j in range(len(data[i])):
				try:
					if data[i][j] == "|":
						if data[i+1][j] != "^":
							buffer[i+1][j] = "|"
						else:
							splits[(i,j)] = 1
							buffer[i+1][j-1] = "|"
							buffer[i+1][j+1] = "|"
				except:
					pass
		display(buffer)
		print(splits)

	return len(splits.keys())

def part2(data):
	answer = 0

	return answer

data = read_data(__file__, "2025")
data = handle(data)
display(data)
print(part1(data))
print(part2(data))