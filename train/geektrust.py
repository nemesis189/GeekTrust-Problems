from src.get_input import *
from src.train.train import get_train_obj, merge_train

def main():
	train_A_bogies, train_B_bogies = get_train_lineups()
	train_A = get_train_obj('A', train_A_bogies)
	train_B = get_train_obj('B', train_B_bogies)

	train_A.print_arrival_at_hyd()
	train_B.print_arrival_at_hyd()
	merge_train(train_A, train_B)	
	
if __name__ == "__main__":
	main()