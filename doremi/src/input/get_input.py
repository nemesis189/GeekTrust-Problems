from sys import argv

def get_commands():
	if len(argv) != 2:
		raise Exception("File path not entered")

	args_position = 1
	file_path = argv[args_position]
	f = open(file_path, 'r')
	Lines = f.readlines()

	commands = [process_command(line) for line in Lines]
	return commands

def process_command(line):
	command = line.strip('\n').split(' ')
	return command
	