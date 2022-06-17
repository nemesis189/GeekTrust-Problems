from src.member.Member import Member

def run_commands(list_of_commands, house):
    for command_line in list_of_commands:
        cmd = command_line[0]

        if cmd == "MOVE_IN":
            new_member = Member(command_line[1])
            house.move_in(new_member)
        
        elif cmd == "SPEND":
            amount = int(command_line[1])
            spent_by = house.get_member(command_line[2])
            spent_for = []
            for m in command_line[3:]:
                member = house.get_member(m)
                if member:
                    spent_for.append(member)
                else:
                    continue

            spent_by.spend(amount, spent_for)
        
        elif cmd == "DUES":
            member = house.get_member(command_line[1])
            member.show_dues(house=house)

        elif cmd == "CLEAR_DUE":
            ower = house.get_member(command_line[1])
            lender = house.get_member(command_line[2])
            amount = int(command_line[3])

            lender.clear_dues(ower, amount)
        
        elif cmd == "MOVE_OUT":
            house.move_out(command_line[1])
    
    return house