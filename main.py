from algorithm import *

#Driver test###########

#input = list of numbers
input = [3,4,2,3,4,3,2,8,6,3,2,8,3,5,1,2,6]
#number = target number
number = 682889
#advanced search
res = False
while not res:
    struct = secu_ops(input, number)
    res = struct[0]
    print_sequence(input, struct[1], number)
    number += 1
