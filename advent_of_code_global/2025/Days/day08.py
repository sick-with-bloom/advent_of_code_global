from utils.datahandler import read_data
from math import sqrt, inf

def handle(data):
	data = data.split("\n")
	data = [tuple([int(num) for num in line.split(",")]) for line in data]
	return data

def distance(point1, point2):
	return sqrt(pow(point2[0]-point1[0],2) + pow(point2[1]-point1[1],2) + pow(point2[2]-point1[2],2))

def part1(data):
	answer = 0
	circuits = {point:[] for point in data}
	print(circuits)
	for i in range(len(data)):
		closest = inf
		closestPoint = None
		for j in range(len(data)):
			dist = distance(data[i], data[j])
			if dist != 0 and dist < closest and data[j] not in circuits[data[i]]:
				closest = dist
				closestPoint = data[j]
			print(data[i], data[j], distance(data[i], data[j]))

		circuits[data[i]].append(closestPoint)
		circuits[closestPoint].append(data[i])
		for _ in circuits.keys():
			print(_,":",circuits[_])
		input()
	return answer

def part2(data):
	answer = 0

	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(part1(data))
print(part2(data))