from tests.test_train import create_test_trains
import unittest

class TestTrainRoute(unittest.TestCase):
    def setUp(self):
        self.train_A, self.train_B = create_test_trains()
        self.route_A, self.route_B  = self.train_A.route, self.train_B.route
    
    def test_train_route(self):
        expected_route_A = {'CHENNAI': {'code': 'CHN', 'distance': 0}, 'SALEM': {'code': 'SLM', 'distance': 350}, 'BANGALORE': {'code': 'BLR', 'distance': 550}, 'KURNOOL': {'code': 'KRN', 'distance': 900}, 'HYDERABAD': {'code': 'HYB', 'distance': 1200}, 'NAGPUR': {
            'code': 'NGP', 'distance': 1600}, 'ITARSI': {'code': 'ITJ', 'distance': 1900}, 'BHOPAL': {'code': 'BPL', 'distance': 2000}, 'AGRA': {'code': 'AGA', 'distance': 2500}, 'NEW DELHI': {'code': 'NDL', 'distance': 2700}}
        expected_route_B = {'TRIVANDRUM': {'code': 'TVC', 'distance': 0}, 'SHORANUR': {'code': 'SRR', 'distance': 300}, 'MANGALORE': {'code': 'MAQ', 'distance': 600}, 'MADGAON': {'code': 'MAO', 'distance': 1000}, 'PUNE': {'code': 'PNE', 'distance': 1400}, 'HYDERABAD': {'code': 'HYB', 'distance': 2000}, 'NAGPUR': {
            'code': 'NGP', 'distance': 2400}, 'ITARSI': {'code': 'ITJ', 'distance': 2700}, 'BHOPAL': {'code': 'BPL', 'distance': 2800}, 'PATNA': {'code': 'PTA', 'distance': 3800}, 'NEW JALPAIGURI': {'code': 'NJP', 'distance': 4200}, 'GUWAHATI': {'code': 'GHY', 'distance': 4700}}
        self.assertEqual(self.route_A.train_route, expected_route_A)
        self.assertEqual(self.route_B.train_route, expected_route_B)
    
    def test_stops_before_hyd(self):
        expected_stops_route_A = ['CHN', 'SLM', 'BLR', 'KRN']
        expected_stops_route_B = ['TVC', 'SRR', 'MAQ', 'MAO', 'PNE']

        self.assertEqual(self.route_A.stops_before_hyd, expected_stops_route_A)
        self.assertEqual(self.route_B.stops_before_hyd, expected_stops_route_B)
