from sys import argv
from src.input.get_input import get_commands
from src.streaming_app.StreamingApp import StreamingApp

def main():
	commands = get_commands()
	stream_app = StreamingApp()

	for cmd in commands:
		if cmd[0] == 'START_SUBSCRIPTION':
			stream_app.set_start_date(cmd[1])
		
		elif cmd[0] == 'ADD_SUBSCRIPTION':
			stream_app.add_subscription(cmd[1], cmd[2])
		
		elif cmd[0] == 'ADD_TOPUP':
			stream_app.add_topup(cmd[1], cmd[2])
		
		elif cmd[0] == 'PRINT_RENEWAL_DETAILS':
			stream_app.print_renewal_details()

	
if __name__ == "__main__":
	main()