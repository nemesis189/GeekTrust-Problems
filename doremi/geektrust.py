from sys import argv
from src.input.get_input import get_commands
from src.input.run_commands import run_commands
from src.streaming_app.StreamingApp import get_streaming_app

def main():
	commands = get_commands()
	stream_app = get_streaming_app()
	run_commands(commands, stream_app)
	

	
if __name__ == "__main__":
	main()