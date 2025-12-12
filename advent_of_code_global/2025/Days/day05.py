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
				#print(f"{i} is in {r}")
				break
		if not spoiled:
			answer += 1
	
	return answer

def day02(data):
	answer = 0
	ranges = data[0]
	ranges = sorted(ranges, key=lambda x:x[0])

	merged_ranges = []
	start = 0
	end = 0
	while start != len(ranges):
		start_range = ranges[start]
		end = start + 1
		while end < len(ranges):
			end_range = ranges[end]
			if end_range[0] < start_range[1] < end_range[1]:
				pass
			else:





	print("***",ranges)

	return answer
	#336156454845765
	#359913027576322

	

data = read_data(__file__, "2025")
data = handle(data)
print(day01(data))
print(day02(data))

#wrong answer:
#421613495822128