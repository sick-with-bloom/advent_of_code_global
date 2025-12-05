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

def checkForOverlaps(old,new):
	overlaps = 0
	for r in old:
		#different overlap cases
		# n--r==n==r starts before ends within
		if new[0] < r[0] and r[0] < new[1] < r[1]:
			print("\t\toverlap! (type 1)", r, new)
			overlaps += 1
			r[0] = new[0]
		# n--r==r--n starts before ends after
		elif new[0] < r[0] and r[1] < new[1]:
			print("\t\toverlap! (type 2)", r, new)
			overlaps += 1
			r[0] = new[0]
			r[1] = new[1]
		# r==n==r--n starts within ends after
		elif r[0] < new[0] < r[1] and r[1] < new[1]:
			print("\t\toverlap! (type 3)", r, new)
			overlaps += 1
			r[1] = new[1]
		# r==n==n==r starts within ends within
		elif r[0] < new[0] < r[1] and r[0] < new[1] < r[1]:
			print("\t\toverlap! (type 4)", r, new)
			overlaps += 1
		#print(new,r)
	return overlaps

def day02(data):
	answer = 0
	ranges = []
	for new in data[0]:
		#print(new)
		#iterate across ranges list
		#if new overlaps, modify range to include new max and/or min
		#if new has no overlaps, add to ranges list
		print("first order check")
		overlaps = checkForOverlaps(ranges, new)
		if overlaps == 0:
			#print("adding",new)
			ranges.append(new)
			#now check for any redundant ranges
		newRanges = []
		for oldNew in ranges:
			print("second order check")
			overlaps = checkForOverlaps(newRanges, oldNew)
			print(oldNew,"has",overlaps,"overlaps with",newRanges)
			if overlaps == 0:
				newRanges.append(oldNew)
		ranges = [_ for _ in newRanges]
		print(newRanges)
		print("...")
	print(ranges)

	return sum([r[1] - r[0] + 1 for r in ranges])

	

data = read_data(__file__, "2025")
data = handle(data)
print(data)
print(day01(data))
print(day02(data))

#wrong answer:
#421613495822128