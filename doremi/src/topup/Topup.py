class Topup:
	def __init__(self, topup_category, no_of_months):
		self.topup_category = topup_category
		self.no_of_months = int(no_of_months)
		self.no_of_devices = self.get_no_of_devices(topup_category)
		self.cost_per_month = self.get_cost_per_month()		

	def get_no_of_devices(self, topup_category):
		if topup_category == 'FOUR_DEVICE':
			return 4
		elif topup_category == 'TEN_DEVICE':
			return 10

	def get_cost_per_month(self):
		if self.topup_category == 'FOUR_DEVICE':
			return 50
		elif self.topup_category == 'TEN_DEVICE':
			return 100
	
	def get_total_topup_cost(self):
		return self.no_of_months * self.cost_per_month

def get_topup(topup_category, no_of_months):
	topup = Topup(topup_category, no_of_months)
	return topup