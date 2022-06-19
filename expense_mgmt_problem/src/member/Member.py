
class Member:
	def __init__(self, name):
		self.name = name
		self.dues_remaining = 0
		self.owes = {}

	def set_member_house(self, house):
		self.house = house
	
	def spend(self, amount, spent_for):
		print
		n = len(spent_for) + 1
		amount_per_head = round(amount/n)
		for spent_for_mem in spent_for:
			self.update_amounts_for_spender(amount_per_head, spent_for_mem)
			self.update_amounts_for_other_member(spent_for_mem)
		
		self.update_dues_remaining()
		print("SUCCESS")

	def update_amounts_for_spender(self, amount_per_head, spent_for_mem):
		owed_amount_set_flag = 0
		for mem, owed_amount in self.owes.items():
			if owed_amount > 0 :
				owed_amount_set_flag = 1
				self.update_owed_amount_of_members_involved(mem, spent_for_mem, owed_amount, amount_per_head)
		if not owed_amount_set_flag:
			spent_for_mem.member_owes(self.name, amount_per_head)

	def update_amounts_for_other_member(self, spent_for_mem):
		others = [mem for mem in spent_for_mem.owes if mem != spent_for_mem.name and mem != self.name]
		other_member_owed = self.house.get_member_in_house(others[0]) if others else None
		if other_member_owed:

			if spent_for_mem.owes[other_member_owed.name] > 0:
				for mem, owed_amount in other_member_owed.owes.items():
					if owed_amount > 0:
						other_member_owed.update_owed_amount_of_members_involved(mem, spent_for_mem, owed_amount, spent_for_mem.owes[other_member_owed.name], other=True)


	def update_owed_amount_of_members_involved(self, lender, ower, owed_amount, received_amount, other=False):
		remainder_amt = received_amount - owed_amount if received_amount > owed_amount else 0
		if remainder_amt > 0:
			if lender != ower.name:
				ower.member_owes(lender, owed_amount)
			ower.member_owes(self.name, remainder_amt)
			self.owes[lender] -= owed_amount
			if other:
				ower.owes[self.name] -= received_amount
		else:
			if lender != ower.name:
				ower.member_owes(lender, received_amount)
			self.owes[lender] -= received_amount
			if other:
				ower.owes[self.name] -= received_amount



	def member_owes(self, lender, amount):
		if lender not in self.owes :
			self.owes[lender] = 0
		amount_already_lent = self.owes[lender]
		self.owes.update({lender: amount_already_lent + amount})
		self.update_dues_remaining()


	def show_dues(self, house=None, print_msg=True):
		dues = []

		if house and print_msg == True:
			self.print_dues(house)
		else:
			for (lender, amount) in self.owes.items():
				dues.append((lender, amount))
			return dues

	def print_dues(self, house):
		dues = []
		all_members = [m.name for m in house.members if m.name != self.name]
		for memb in all_members:
			if memb not in self.owes.keys():
				dues.append((memb, 0))
			else:
				dues.append((memb, self.owes[memb]))
		
		dues.sort(key = lambda x : x[1], reverse=True)
		dues = self.sort_by_name(dues)

		for (lender, amount) in dues:
			print(f'{lender} {amount}')

	def sort_by_name(self, dues):
		due_amount_list = [x[1] for x in dues]
		amount_count = { amt:due_amount_list.count(amt) for amt in due_amount_list }
		new_sorted_list = []
		count_flag = 0
		for name,amount in dues:
			if count_flag != 0:
				count_flag -= 1
				continue

			initial_index = due_amount_list.index(amount)
			if amount_count[amount] > 1:
				count_flag = amount_count[amount]
				sub_list = dues[initial_index : initial_index + amount_count[amount]]
				sub_list.sort(key=lambda x:x[0])
				new_sorted_list += sub_list
			else:
				new_sorted_list.append((name, amount))

		return new_sorted_list


	def clear_dues(self, member, amount):
		dues = member.show_dues(print_msg=False)
		due_against = [due_amt for (lender, due_amt) in dues if lender==self.name][0]
		if amount <= due_against:
			member.owes[self.name] -= amount 
			print(member.owes[self.name])
		else:
			print('INCORRECT_PAYMENT')

		member.update_dues_remaining()
	
	def update_dues_remaining(self):
		amount_sum = 0
		for mem, amount in self.owes.items():
			if mem != self.name:
				amount_sum += amount
			self.dues_remaining = amount_sum

	def set_owes_list(self):
		for member in self.house.members:
			member.owes.update({self.name: 0})
			self.owes.update({member.name: 0})
		
