from src.member.Member import Member
from src.utils import get_members_spent_for


command_name_index = 0
command_1_index = 1
command_2_index = 2
command_3_index = 3

def validate_members(member_list):
    return False if None in member_list else True


def run_commands(list_of_commands, house):
    for command_line in list_of_commands:
        cmd = command_line[command_name_index]

        if cmd == "MOVE_IN":
            new_member = Member(command_line[command_1_index])
            new_member.set_member_house(house)
            new_member.set_owes_list()
            house.move_in(new_member)
        
        elif cmd == "SPEND":
            amount = int(command_line[command_1_index])
            spent_by = house.get_member_in_house(command_line[command_2_index])
            spent_for = get_members_spent_for(house, command_line)
            members = [spent_by] + spent_for

            members_valid_check = validate_members(members)
            if members_valid_check:  
                spent_by.spend(amount, spent_for)
            else:
                print("MEMBER_NOT_FOUND")
            
        
        elif cmd == "DUES":
            member = house.get_member_in_house(command_line[command_1_index])

            members_valid_check = validate_members([member])
            if members_valid_check:  
                member.show_dues(house=house)
            else:
                print("MEMBER_NOT_FOUND")
            

        elif cmd == "CLEAR_DUE":
            ower = house.get_member_in_house(command_line[command_1_index])
            lender = house.get_member_in_house(command_line[command_2_index])
            amount = int(command_line[command_3_index])
            members = [ower, lender]

            members_valid_check = validate_members(members)
            if members_valid_check:  
                lender.clear_dues(ower, amount)
            else:
                print("MEMBER_NOT_FOUND")
        
        elif cmd == "MOVE_OUT":
            member = house.get_member_in_house(command_line[command_1_index])
            members_valid_check = validate_members([member])
            if members_valid_check:  
                house.move_out(command_line[command_1_index])
            else:
                print("MEMBER_NOT_FOUND")
    
    return house