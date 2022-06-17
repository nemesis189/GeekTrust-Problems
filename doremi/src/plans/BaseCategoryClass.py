from src.plans.plans_classes import FreePlan, PersonalPlan, PremiumPlan

class BaseCategoryClass:
	def __init__(self, name, personal_plan_price, premium_plan_price):
		self.free_plan = FreePlan(name)
		self.personal_plan = PersonalPlan(name, personal_plan_price)
		self.premium_plan = PremiumPlan(name, premium_plan_price)
	
	def get_required_plan(self, plan):
		if plan == 'FREE':
			return self.free_plan

		elif plan == 'PERSONAL':
			return self.personal_plan

		elif plan == 'PREMIUM':
			return self.premium_plan