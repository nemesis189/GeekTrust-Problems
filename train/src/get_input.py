from sys import argv

def get_input_args():
	location_index = 1
	if len(argv) != 2:
			raise Exception("File path not entered")
	file_path = argv[location_index]
	f = open(file_path, 'r')
	lines = f.readlines()
	return lines

def process_input_lines(lines):
	train_A_lineup_index = 0
	train_B_lineup_index = 1
	bogies_start_from_index = 1
	splitlines = [l.strip('\n') for l in lines]
	list_of_commands = [ line.split(' ') for line in splitlines if len(line)]
	return list_of_commands[train_A_lineup_index][bogies_start_from_index:], list_of_commands[train_B_lineup_index][bogies_start_from_index:]

def get_train_lineups():
	input_lines = get_input_args()
	train_A, train_B = process_input_lines(input_lines)
	return train_A, train_B