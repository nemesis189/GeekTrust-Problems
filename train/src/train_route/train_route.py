import json

class TrainRoute:
	def __init__(self, train):
		self.train = train.train_name
		self.stops_before_hyd = []
		self.train_A_and_B_routes = {}

	def set_train_route(self):
		self.train_route = self.get_route_data_from_json()
	
	def get_route_data_from_json(self):
		return_data = None
		for train in ['A', 'B']:
			f = open(f'src/train_route/train_{train}_route.json')
			data = json.load(f)
			if train == self.train:
				return_data = data
			f.close()
			if train not in self.train_A_and_B_routes:
				self.train_A_and_B_routes.update({train: data})
		return return_data

	def set_stops_before_hyd(self):
		for stop, detail in self.train_route.items():
			if stop == 'HYDERABAD':
				return
			
			self.stops_before_hyd.append(detail['code'])
	
	def get_bogey_name(self, bogey):
		bogey_name = ''
		for train in self.train_A_and_B_routes:
			bogey_name = [name for name, details in self.train_A_and_B_routes[train].items() if details['code'] == bogey]
			if bogey_name:
				return bogey_name[0]

		print("BOGEY NOT FOUND")
		return None


def get_route_for_train(train):
	route = TrainRoute(train)
	route.set_train_route()
	route.set_stops_before_hyd()
	return route