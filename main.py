from algorithm import *


input = [1,1,1]
number = 3
output_structure = secu_ops(input, input.__len__() - 1, number)
print_sequence(input, output_structure[1], number)
