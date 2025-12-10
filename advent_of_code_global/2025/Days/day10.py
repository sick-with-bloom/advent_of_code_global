from utils.datahandler import read_data
from math import sqrt, inf

def handle(data):
	data = data.split(" ")
	data = [data[0][1:-1], data[1:-1]]
	data[1] = [tuple([int(num) for num in line[1:-1].split(",")]) for line in data[1]]
	return data

def stateChange(state,input):
	state = list(state)
	for num in input:
		if state[num] == ".":
			state[num] = "#"
		else:
			state[num] = "."
	return "".join(state)

def part1(data):
	answer = 0
	endState = data[0]
	print("end state =",endState)
	buttons = data[1]
	length = len(endState)
	states = {}
	for i in range(2**length):
		state = bin(i)[2:].zfill(length)
		state = "".join(["#" if _ == "1" else "." for _ in state ])
		states[state] = {}

	for state in states.keys():
		for button in buttons:
			states[state][button] = stateChange(state, button)

	for state in states.keys():
		print(state)
		start = states[state]
		for transition in start.keys():
			end = start[transition]
			print("\t",transition,"==>",end)
			if end == endState:
				print("\t\t^^^^^")

	return answer

def part2(data):
	answer = 0

	return answer

data = read_data(__file__, "2025")
data = handle(data)
print(data)
print(part1(data))
print(part2(data))