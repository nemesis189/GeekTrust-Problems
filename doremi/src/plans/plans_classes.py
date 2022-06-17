from src.plans.BasePlan import BasePlan

class FreePlan(BasePlan):
	def __init__(self, subscription_category):
		super().__init__('FREE', subscription_category, 0, 1)    

class PersonalPlan(BasePlan):
	def __init__(self, subscription_category, price):
		super().__init__('PERSONAL', subscription_category, price, 1)    

class PremiumPlan(BasePlan):
	def __init__(self, subscription_category, price):
		super().__init__('PREMIUM', subscription_category, price, 3)    