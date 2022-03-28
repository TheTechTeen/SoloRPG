def message(message):
    input(message + " ")

def choose_dict(options):
		x = 1
		if len(options) == 0:
			return "empty"
		if len(options) == 1:
			message(list(options.keys())[0])
			return list(options.values())[0]
		for option in options.keys():
			print(f"{x}. {option}")
			x += 1
		try:
			answer = int(input("Which option? "))
			return options[list(options.keys())[answer-1]]
		except:
			message("Invalid Option")
			return choose_dict(options)

def choose_list(options):
		x = 1
		if len(options) == 0:
			return "empty"
		if len(options) == 1:
			message(options[0])
			return options[0]
		for option in options:
			print(f"{x}. {option}")
			x += 1
		try:
			answer = int(input("Which option? "))
			return options[answer-1]
		except:
			message("Invalid Option")
			return choose_list(options)