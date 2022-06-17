from sys import argv

def main():
    
    """
    Sample code to read inputs from the file
    """

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    list_of_commands = get_commands(Lines)

    run_commands(list_of_commands)

def get_commands(lines):
    splitlines = [l.strip('\n') for l in lines]
    list_of_commands = [ line.split(' ') for line in splitlines]

    return list_of_commands

# Available commands:
# MOVE_IN <name-of-the-member>
# SPEND <amount> <spent-by> <spent-for-member1> <spent-for-member2>
# DUES <member-who-owes>
# CLEAR_DUE <member-who-owes> <member-who-lent> <amount>
# MOVE_OUT <name-of-existing-member>

def run_commands(list_of_commands):
    house = House()

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
            member = self.get_member(member_name)
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
    
    def get_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        print("MEMBER_NOT_FOUND")



class Member:
    def __init__(self, name):
        self.name = name
        self.dues_remaining = 0
        self.owes = {}
    
    def spend(self, amount, spent_for):
        spent_by = self
        n = len(spent_for) + 1
        amount_per_head = round(amount/n)
        owed_amt_set_flag = 0

        for spent_for_mem in spent_for:
            for mem, owed_amt in spent_by.owes.items():
                if owed_amt > 0:
                    owed_amt_set_flag = 1
                    remainder_amt = amount_per_head - owed_amt if amount_per_head > owed_amt else 0
                    if remainder_amt > 0:
                        spent_for_mem.member_owes(mem, owed_amt)
                        spent_for_mem.member_owes(spent_by.name, remainder_amt)
                        spent_by.owes[mem] -= owed_amt
                    else:
                        spent_for_mem.member_owes(mem, amount_per_head)
                        spent_by.owes[mem] -= amount_per_head

            if not owed_amt_set_flag:
                spent_for_mem.member_owes(spent_by.name, amount_per_head)
        
        self.update_dues_remaining()
        print("SUCCESS")


    def member_owes(self, lender, amount):
        if lender not in self.owes:
            self.owes[lender] = 0
        amount_already_lent = self.owes[lender]
        self.owes.update({lender: amount_already_lent + amount})
        self.update_dues_remaining()


    def show_dues(self, house=None, print_msg=True):
        dues = []
        all_members = None

        if house and print_msg == True:
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

        else:
            for (lender, amount) in self.owes.items():
                dues.append((lender, amount))
            return dues


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
        self.dues_remaining = sum(self.owes.values())



if __name__ == "__main__":
    main()