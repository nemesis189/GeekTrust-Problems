class House:
	def __init__(self):
		self.members = []
	
	def move_in(self, member):
		if len(self.members) < 3:
			self.members.append(member)
			print('SUCCESS')
		else:
			print('HOUSEFUL')
	
	def move_out(self, member_name):
		if member_name not in [m.name for m in self.members]:
			print("MEMBER_NOT_FOUND")
			return

		if len(self.members) > 0:
			member = self.get_member_in_house(member_name)
			owed_amount = self.get_owed_amount(member_name)
			if member.dues_remaining == 0 and owed_amount == 0:
				filter(lambda x: x.name == member.name, self.members)
				print('SUCCESS')
			else:
				print('FAILURE')
		else:
			print('FAILURE')

	def get_owed_amount(self, name):
		amount = 0
		for member in self.members:
			if name in member.owes:
				amount += member.owes[name]
		return amount
	
	def get_member_in_house(self, name):
		for member in self.members:
			if member.name == name:
				return member
		return None


