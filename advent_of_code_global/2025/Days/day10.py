from operator import ne
from utils.datahandler import read_data
from math import sqrt, inf

def handleInput(data):
	data = data.split("\n")
	data = [handleLine(line) for line in data]
	return data

def handleLine(data):
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

def display(states):
	for state in states.keys():
		print(state)
		start = states[state]
		for transition in start.keys():
			end = start[transition]
			print("\t",transition,"==>",end)

def solve(data):
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
			end = stateChange(state, button)
			states[state][button] = end

	current = endState

	queue = [state for state in states.keys()]
	distances = {state : inf for state in states.keys()}
	distances[current] = 0

	queue = [state for distance, state in sorted(zip([distances[_] for _ in queue],queue))]

	while current != "."*length:
		current = queue.pop(0)
		neighbours = [state for state in states[current].values()]
		for neighbour in neighbours:
			oldDistance = distances[neighbour]
			newDistance = distances[current] + 1
			if newDistance < oldDistance:
				distances[neighbour] = newDistance

		queue = [state for distance, state in sorted(zip([distances[_] for _ in queue],queue))]
	return distances["."*length]

def part1(data):
	answer = 0
	for line in data:
		print(line)
		answer_ = solve(line)
		print(answer_)
		answer += answer_
	return answer

def part2(data):
	answer = 0

	return answer

data = read_data(__file__, "2025")
data = handleInput(data)
print(data)
print(part1(data))
print(part2(data))