import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "outputs/ch20_t09o_output.txt")

with open(file_path_name, "w") as my_file:
    my_file.write("My Data!")

if my_file.closed == False:
    my_file.close()

print(my_file.closed)
