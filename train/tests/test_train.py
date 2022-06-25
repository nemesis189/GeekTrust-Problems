from src.get_input import process_input_lines
from src.train.train import get_train_obj
import unittest

class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train_A, self.train_B = create_test_trains()

    def test_train_name(self):
        self.assertEqual(self.train_A.train_name, 'A')
        self.assertEqual(self.train_B.train_name, 'B')
    
    def test_passenger_bogies(self):
        expected_bogies_A = ['ENGINE', 'SLM', 'BLR', 'KRN', 'HYB', 'SLM', 'NGP', 'ITJ']
        expected_bogies_B = ['ENGINE', 'SRR', 'MAO', 'NJP', 'PNE', 'PTA']

        self.assertEqual(self.train_A.passenger_bogies, expected_bogies_A)
        self.assertEqual(self.train_B.passenger_bogies, expected_bogies_B)
    
    def test_order_of_arrival_at_hyd(self):
        expected_order_A = ['ENGINE', 'HYB', 'NGP', 'ITJ']
        expected_order_B = ['ENGINE', 'NJP', 'PTA']
        
        self.assertEqual(self.train_A.order_of_arrival_at_hyd, expected_order_A)
        self.assertEqual(self.train_B.order_of_arrival_at_hyd, expected_order_B)

    def test_bogies_after_hyd_with_dist(self):
        expected_A = [('ITJ', 700), ('NGP', 400), ('HYB', 0)]
        expected_B = [('NJP', 2200), ('PTA', 1800)]

        self.assertEqual(self.train_A.bogies_after_hyd_with_dist, expected_A)
        self.assertEqual(self.train_B.bogies_after_hyd_with_dist, expected_B)

def create_test_trains():
    ip = ["TRAIN_A ENGINE SLM BLR KRN HYB SLM NGP ITJ\n","TRAIN_B ENGINE SRR MAO NJP PNE PTA\n"]
    train_A_bogies, train_B_bogies = process_input_lines(ip)
    train_B = get_train_obj('B', train_B_bogies)
    train_A = get_train_obj('A', train_A_bogies)

    return train_A, train_B
