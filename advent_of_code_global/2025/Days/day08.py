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
	
	boxes = data
	distances = {tuple([boxes[i], boxes[j]]): distance(boxes[i], boxes[j])  for i in range(len(boxes)) for j in range(len(boxes)) if i != j}
	distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
	for d in distances.keys():
		print(d, distances[d])
	
	return answer

def part2(data):
	answer = 0

	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(part1(data))
print(part2(data))