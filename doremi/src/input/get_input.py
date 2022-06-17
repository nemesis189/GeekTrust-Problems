from sys import argv

def get_commands():
	if len(argv) != 2:
		raise Exception("File path not entered")

	file_path = argv[1]
	f = open(file_path, 'r')
	Lines = f.readlines()

	commands = [process_command(line) for line in Lines]
	return commands

def process_command(line):
	command = line.strip('\n').split(' ')
	return command
	