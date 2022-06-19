def get_members_spent_for(house, command_line):
	spent_for = []
	for m in command_line[3:]:
		member = house.get_member_in_house(m)
		spent_for.append(member)
	return spent_for