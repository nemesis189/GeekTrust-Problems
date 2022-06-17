class BasePlan:
	def __init__(self, plan_name, subscription_category, price, months):
		self.plan_name = plan_name
		self.price = 0 if subscription_category == 'FREE' else price
		self.months = months
		self.subscription_category = subscription_category



