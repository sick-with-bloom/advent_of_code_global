from utils.datahandler import read_data
from math import sqrt, inf

def rect(corner1, corner2):
	x = abs(corner1[0] - corner2[0] + 1)
	y = abs(corner1[1] - corner2[1] + 1)
	area = x * y
	#print(corner1,corner2,area)
	return area

def makeRect(corner1, corner2):
	thisRect = ((corner1[0], corner1[1]),(corner1[0], corner2[1]),(corner2[0], corner2[1]),(corner2[0], corner1[1]),(corner1[0], corner1[1]))
	print(corner1, corner2, thisRect)
	return thisRect

def handle(data):
	data = data.split("\n")
	data = [tuple([int(num) for num in line.split(",")]) for line in data]
	return data

def part1(data):
	largest = None
	largestArea = 0
	for i in range(len(data)):
		for j in range(len(data)):
			area = rect(data[i], data[j])
			if area > largestArea:
				largest = (data[i], data[j])
				largestArea = area
	return largestArea

def part2(data):
	answer = 0
	width = max([line[0] for line in data])
	height = max([line[1] for line in data])
	shape = [data[i%len(data)] for i in range(len(data) + 1)]
	possibleRects = [makeRect(data[i], data[j]) for i in range(len(data)) for j in range(len(data)) if i != j]
	print(shape)
	for r in possibleRects:
		print(r)
	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(part1(data))
print(part2(data))