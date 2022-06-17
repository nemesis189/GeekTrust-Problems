from sys import argv
from src.input_commands.GetProccessedCommands import get_commands
from src.input_commands.RunCommands import run_commands
from src.house.House import House
from src.member.Member import Member

def main():

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    list_of_commands = get_commands(Lines)
    house = House()
    run_commands(list_of_commands, house)


if __name__ == "__main__":
    main()