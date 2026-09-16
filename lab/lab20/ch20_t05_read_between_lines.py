import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "inputs/ch20_t05o_output.txt")

my_file = open(file_path_name, "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()
