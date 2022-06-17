
class Member:
    def __init__(self, name):
        self.name = name
        self.dues_remaining = 0
        self.owes = {}
    
    def spend(self, amount, spent_for):
        n = len(spent_for) + 1
        amount_per_head = round(amount/n)
        owed_amt_set_flag = 0

        for spent_for_mem in spent_for:
            for mem, owed_amt in self.owes.items():
                if owed_amt > 0:
                    owed_amt_set_flag = 1
                    remainder_amt = amount_per_head - owed_amt if amount_per_head > owed_amt else 0
                    if remainder_amt > 0:
                        spent_for_mem.member_owes(mem, owed_amt)
                        spent_for_mem.member_owes(self.name, remainder_amt)
                        self.owes[mem] -= owed_amt
                    else:
                        spent_for_mem.member_owes(mem, amount_per_head)
                        self.owes[mem] -= amount_per_head

            if not owed_amt_set_flag:
                spent_for_mem.member_owes(self.name, amount_per_head)
        
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

