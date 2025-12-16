from utils.datahandler import read_data
import itertools

def handle(data):
	data = data.split("\n\n")
	ranges = data[0].split("\n")
	ingredients = data[1].split("\n")
	ingredients = [int(ingredient) for ingredient in ingredients]
	ranges = [[int(num) for num in line.split("-")] for line in ranges]
	return [ranges,ingredients]

def day01(data):
	answer = 0
	ranges = data[0]
	ranges = [range(line[0],line[1]+1) for line in ranges]
	ingredients = data[1]
	for i in ingredients:
		spoiled = True
		for r in ranges:
			if i in r:
				spoiled = False
				break
		if not spoiled:
			answer += 1
	
	return answer

def day02(data):
	answer = 0
	lines = data[0]
	lines = sorted(lines, key=lambda x:x[0])

	i = 0
	while i < len(lines) - 1:
		start = lines[i]
		end = lines[i + 1]
		if lines[i][1] >= lines[i+1][0]:
			lines[i] = [start[0], max([start[1], end[1]])]
			lines.pop(i+1)
		else:
			i += 1

	answer = sum([line[1] - line[0] + 1 for line in lines])
	return answer

	

data = read_data(__file__, "2025")
data = handle(data)
print(day01(data))
print(day02(data))
