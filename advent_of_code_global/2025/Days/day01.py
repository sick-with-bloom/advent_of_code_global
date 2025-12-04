from utils.datahandler import read_data

def handle(data):
	data = data.split("\n")
	data = [[line[0], int(line[1:])] for line in data]
	return data

directions = {"L":-1,"R":1}

def solve(data, part):
	answer = 0
	time = 50
	for line in data:
		direction = directions[line[0]]
		end = time + (direction * line[1])
		if part == 1:
			time = end
			if time % 100 == 0:
				answer += 1
		elif part == 2:
			while time != end:
				time += direction
				if time % 100 == 0:
					answer += 1
	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(solve(data,1))
print(solve(data,2))