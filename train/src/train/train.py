from src.train_route.train_route import TrainRoute, get_route_for_train

class Train:
    def __init__(self, A_or_B, bogies):
        self.train_name = A_or_B
        self.passenger_bogies = bogies
        self.bogies_after_hyd_with_dist = []
        self.order_of_arrival_at_hyd = []

    def set_route(self):
        self.route = get_route_for_train(self)

    def get_order_of_arrival_at_hyd(self):
        for stop in self.passenger_bogies:
            if stop not in self.route.stops_before_hyd or stop == 'ENGINE':
                self.order_of_arrival_at_hyd.append(stop)
        
    def set_bogies_after_hyd_with_dist(self):
        for bogey in self.order_of_arrival_at_hyd:
            if bogey != 'ENGINE':
                self.bogies_after_hyd_with_dist.append((bogey,self.calculate_dist_from_hyd(bogey)))
        self.bogies_after_hyd_with_dist.sort(key=lambda x:x[1], reverse=True)
    
    def calculate_dist_from_hyd(self, bogey):
        bogey_name = self.route.get_bogey_name(bogey)
        if bogey_name not in self.route.train_route:
            other_train = [x for x in ['A', 'B'] if x != self.train_name][0]
            return self.route.train_A_and_B_routes[other_train][bogey_name]['distance'] - self.route.train_A_and_B_routes[other_train]['HYDERABAD']['distance']
        return self.route.train_route[bogey_name]['distance'] - self.route.train_route['HYDERABAD']['distance']

    def print_arrival_at_hyd(self):
        output = f'ARRIVAL TRAIN_{self.train_name}'
        for bogey in self.order_of_arrival_at_hyd:
            output += f' {bogey}'
        print(output)

def get_train_obj(A_or_B, bogies):
    train = Train(A_or_B, bogies)
    train.set_route()
    train.get_order_of_arrival_at_hyd()
    train.set_bogies_after_hyd_with_dist()
    return train

def merge_train(train_A, train_B):
    train_AB = []
    
    train_A_sorted = train_A.bogies_after_hyd_with_dist
    train_B_sorted = train_B.bogies_after_hyd_with_dist
    train_AB = train_A_sorted + train_B_sorted
    train_AB.sort(key=lambda x:x[1], reverse=True)

    output = 'DEPARTURE TRAIN_AB ENGINE ENGINE'
    for bogey in train_AB:
        if bogey[0] != 'HYB':
            output += f' {bogey[0]}'
    
    print(output)



