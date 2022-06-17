def get_commands(lines):
    splitlines = [l.strip('\n') for l in lines]
    list_of_commands = [ line.split(' ') for line in splitlines]
    return list_of_commands