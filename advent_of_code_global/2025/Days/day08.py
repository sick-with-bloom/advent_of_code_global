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
	
	#for each point
	#find its closest neighbour
	#add neighbour to network of first point

	#bfs/dfs until empty, then move to next point not yet accumulated

	for _ in circuits.keys():
		print(_,":",circuits[_])
	return answer

def part2(data):
	answer = 0

	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(part1(data))
print(part2(data))