from utils.datahandler import read_data
import itertools

def handle(data):
	data = data.split("\n")
	data = [list(line) for line in data]
	return data

def count(data):
	return sum([row.count("X") for row in data])

def day01(data):
	answer = 0
	picture = [[_ for _ in line] for line in data]
	for i in range(len(data)):
		for j in range(len(data[i])):
			adj = 0
			for di in [-1, 0, 1]:
				for dj in [-1, 0, 1]:
					if di == 0 and dj == 0:
						continue
					ni, nj = i + di, j + dj
					if 0 <= ni < len(data) and 0 <= nj < len(data[ni]):
						if data[ni][nj] == "@":
							adj += 1
			if data[i][j] == "@" and adj < 4:
				picture[i][j] = "X"
	for row in picture:
		print("".join(row))
	return count(picture)

def day02(data):
	answer = 0
	oldCount = 0
	newCount = -1
	while newCount != oldCount:
		oldCount = newCount
		buffer = [[_ for _ in line] for line in data]
		for i in range(len(data)):
			for j in range(len(data[i])):
				adj = 0
				for di in [-1, 0, 1]:
					for dj in [-1, 0, 1]:
						if di == 0 and dj == 0:
							continue
						ni, nj = i + di, j + dj
						if 0 <= ni < len(data) and 0 <= nj < len(data[ni]):
							if data[ni][nj] == "@":
								adj += 1
				if data[i][j] == "@" and adj < 4:
					buffer[i][j] = "X"
		for row in buffer:
			print("".join(row))
		newCount = count(buffer)
		for i in range(len(data)):
			for j in range(len(data[i])): 
				data[i][j] = buffer[i][j]
		print(oldCount, newCount)
		#input()
	return count(data)

	

data = read_data(__file__, "2025")
data = handle(data)
print(data)
print(day01(data))
print(day02(data))