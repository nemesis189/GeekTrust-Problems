from datetime import datetime
from src.plans.subscription_classes import Music, Video, Podcast
from dateutil.relativedelta import relativedelta

class Subscription:
	def __init__(self, category, plan, start_date):
		self.start_date = start_date
		self.category = category
		self.plan = plan
		self.plan_obj = self.get_subscription(category, plan)
		self.renewal_date = self.get_renewal_date()

	def get_subscription(self, category, plan):
		if category == 'MUSIC':
			plan_obj =  Music().get_required_plan(plan)
			return plan_obj
			
		elif category == 'VIDEO':
			plan_obj =  Video().get_required_plan(plan)
			return plan_obj
			
		elif category == 'PODCAST':
			plan_obj =  Podcast().get_required_plan(plan)
			return plan_obj
			

	def get_renewal_date(self):
		months = self.plan_obj.months
		return self.start_date + relativedelta(months=months) - relativedelta(days=10)


