import sys
from irr_calculator import main
from test_functions import main_assert

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print("Running main_assert (test mode)...")
        main_assert('test_data_files/input_file.txt', 'test_data_files/output_file.txt', 'test_data_files/answer1.txt')
    else:
        print("Running main (normal mode)...")
        main('test_data_files/input_file.txt', 'test_data_files/output_file.txt')
        print("Cauculation Complete")