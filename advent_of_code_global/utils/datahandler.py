def read_data(source, year):
	target = f"{year}/Input/{source[-8:-3]}.txt"
	try:
		return open(target, "r").read()
	except FileNotFoundError:
	    return "File Not Found!"