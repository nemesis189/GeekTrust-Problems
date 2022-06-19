from datetime import datetime
from src.subscription.Subscription import Subscription, get_subscription
from src.topup.Topup import Topup, get_topup
from src.utils import get_formatted_date, get_validated_date

class StreamingApp:
	def __init__(self, start_date=None):
		self.start_date = get_validated_date(start_date) if start_date else None
		self.subscriptions = []
		self.topup = None
		self.renewal_amount = 0

	def add_subscription(self, category, plan):
		if self.start_date:
			duplicate_category_flag = self.validate_duplicate_category(category)
			if not duplicate_category_flag:
				sub = get_subscription(category, plan, self.start_date)
				self.subscriptions.append(sub)
				self.update_renewal_amount(sub.plan_obj.price)
			else:
				print('ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY')
		else:
			print('ADD_SUBSCRIPTION_FAILED INVALID_DATE')

	def add_topup(self, topup_category, no_of_months):
		if self.start_date:
			topup_already_applied_flag = self.validate_if_topup_applied()
			if len(self.subscriptions) == 0:
				print('ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND')

			elif not topup_already_applied_flag:	
				self.topup = get_topup(topup_category, no_of_months)
				self.update_renewal_amount(self.topup.get_total_topup_cost())
			
			else:
				print('ADD_TOPUP_FAILED DUPLICATE_TOPUP')
		else:
			print('ADD_TOPUP_FAILED INVALID_DATE')

	def print_renewal_details(self):
		if len(self.subscriptions) == 0:
			print('SUBSCRIPTIONS_NOT_FOUND')

		else:
			for subscription in self.subscriptions:
				print(f'RENEWAL_REMINDER {subscription.category} {get_formatted_date(subscription.renewal_date)}')
			print(f'RENEWAL_AMOUNT {self.renewal_amount}')
			

	def validate_if_topup_applied(self):
		if self.topup:
			return True
		else:
			return False
		

	def validate_duplicate_category(self, category):
		categories = [sub.category for sub in self.subscriptions]
		if category in categories:
			return True
		else:
			return False
	
	def update_renewal_amount(self, amount):
		self.renewal_amount += amount
	
	def set_start_date(self, start_date):
		self.start_date = get_validated_date(start_date) if start_date else None

def get_streaming_app(start_date=None):
	app = StreamingApp(start_date)
	return app