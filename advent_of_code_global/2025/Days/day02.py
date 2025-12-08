from utils.datahandler import read_data

def handle(data):
	data = data.split(",")
	data = [line.split("-") for line in data]
	data = [[int(num) for num in line] for line in data]
	return data

def isInvalid(code, repMin, repMax):
	for i in range(1,len(code)//2 + 1):
		section = code[0:i]
		valid = False
		repeats = 0
		for j in range(0,len(code),i):
			nextSection = code[j:j+i]
			if section != nextSection:
				valid = True
			else: repeats += 1
		if not valid and repMin <= repeats <= repMax:
			#print(repeats)
			return True

	return False


def part1(data):
	invalid_codes = 0
	for line in data:
		#print(line)
		for i in range(line[0], line[1] + 1):
			#print("\t",i)
			invalid = isInvalid(str(i),2,2)
			if invalid:
				invalid_codes += i 
				print(i)
				#input()

	return invalid_codes

def part2(data):
	invalid_codes = 0
	for line in data:
		#print(line)
		for i in range(line[0], line[1] + 1):
			#print("\t",i)
			invalid = isInvalid(str(i),2,len(str(i)))
			if invalid:
				invalid_codes += i 
				print(i)
				#input()

	return invalid_codes

data = read_data(__file__, "2025")
data = handle(data)
#print(part1(data))
print(part2(data))