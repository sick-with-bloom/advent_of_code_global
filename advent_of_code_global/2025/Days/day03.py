from utils.datahandler import read_data
import itertools

def handle(data):
	data = data.split("\n")
	return data

def day01(data):
	answer = 0
	for line in data:
		highest = 0
		for i in range(len(line)):
			for j in range(i + 1, len(line)):
				num = int(line[i] + line[j])
				if num > highest:
					highest = num
		answer += highest
		print(line, highest)
	return answer

def day02(data):
	answer = 0
	for line in data:
		#line = list(line)
		i = 0
		while len(line) != 12:
			num = line[:12]
			testNum = line[:i] + line[i+1:]
			testNum = testNum[:12]
			print(i, num, testNum)
			if int(testNum) >= int(num):
				line = line[:i] + line[i+1:]
				i -= 1
				print("\t",line)
			#input()
			i += 1
		answer += int(line)
	return answer


data = read_data(__file__, "2025")
data = handle(data)
print(data)
print(day01(data))
print(day02(data))