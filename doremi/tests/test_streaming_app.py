
from io import StringIO 
from src.input.get_input import process_command
from src.input.run_commands import run_commands
from src.streaming_app.StreamingApp import StreamingApp, get_streaming_app
from src.utils import get_formatted_date
import sys
import unittest

class TestStreamingApp(unittest.TestCase):

	def test_start_date(self):
		stream_app = StreamingApp()
		cmd = "START_SUBSCRIPTION 16-06-2022"
		command = process_command(cmd)
		run_commands([command], stream_app)
		formatted_date = get_formatted_date(stream_app.start_date)
		self.assertEqual(formatted_date, '16-06-2022')

	def test_created_subscription_category_and_plan(self):
		stream_app = get_streaming_app()
		cmd = [
			'START_SUBSCRIPTION 16-06-2022\n',
			'ADD_SUBSCRIPTION MUSIC PERSONAL\n',
			'ADD_SUBSCRIPTION VIDEO PREMIUM\n',
			'ADD_SUBSCRIPTION PODCAST FREE\n'
		]
		commands = [process_command(c) for c in cmd]
		run_commands(commands, stream_app)

		sub1, sub2, sub3 = stream_app.subscriptions

		category1 = sub1.category
		plan1 = sub1.plan
		self.assertEqual(category1, 'MUSIC')
		self.assertEqual(plan1, 'PERSONAL')
		
		category2 = sub2.category
		plan2 = sub2.plan
		self.assertEqual(category2, 'VIDEO')
		self.assertEqual(plan2, 'PREMIUM')

		category3 = sub3.category
		plan3 = sub3.plan
		self.assertEqual(category3, 'PODCAST')
		self.assertEqual(plan3, 'FREE')


	def test_added_topup(self):
		stream_app = get_streaming_app()
		cmd = [
			'START_SUBSCRIPTION 16-06-2022\n',
			'ADD_SUBSCRIPTION MUSIC PERSONAL\n',
			'ADD_SUBSCRIPTION VIDEO PREMIUM\n',
			'ADD_SUBSCRIPTION PODCAST FREE\n',
			'ADD_TOPUP FOUR_DEVICE 3\n'
		]
		commands = [process_command(c) for c in cmd]
		run_commands(commands, stream_app)

		topup = stream_app.topup

		topup_category = topup.topup_category
		no_of_months = topup.no_of_months
		no_of_devices = topup.no_of_devices
		cost_per_month = topup.cost_per_month	

		self.assertEqual(topup_category, 'FOUR_DEVICE')
		self.assertEqual(no_of_months, 3)
		self.assertEqual(no_of_devices, 4)
		self.assertEqual(cost_per_month, 50)

	def test_renewal_date(self):
		stream_app = get_streaming_app()
		cmd = [
			'START_SUBSCRIPTION 16-06-2022\n',
			'ADD_SUBSCRIPTION MUSIC PERSONAL\n',
			'ADD_SUBSCRIPTION VIDEO PREMIUM\n',
			'ADD_SUBSCRIPTION PODCAST FREE\n',
			'ADD_TOPUP FOUR_DEVICE 3\n'
		]
		commands = [process_command(c) for c in cmd]
		run_commands(commands, stream_app)

		sub1 = stream_app.subscriptions[0]
		
		check_renewal_date_1 = '06-07-2022'
		formatted_date_1 = get_formatted_date(sub1.renewal_date)
		
		self.assertEqual(check_renewal_date_1, formatted_date_1)

	def test_print_renewal_details(self):
		capturedOutput = StringIO()
		sys.stdout = capturedOutput

		stream_app = get_streaming_app()
		cmd = [
			'START_SUBSCRIPTION 16-06-2022\n',
			'ADD_SUBSCRIPTION MUSIC PERSONAL\n',
			'ADD_TOPUP FOUR_DEVICE 3\n',
			'PRINT_RENEWAL_DETAILS\n'
		]
		commands = [process_command(c) for c in cmd]
		run_commands(commands, stream_app)

		sys.stdout = sys.__stdout__

		expected_output = "RENEWAL_REMINDER MUSIC 06-07-2022\nRENEWAL_AMOUNT 250\n"
		self.assertEqual(capturedOutput.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
