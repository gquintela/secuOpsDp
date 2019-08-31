def secu_ops(input, index, remainder):
    matrix = [[None for i in range(0, remainder + 1)]
              for j in range(0, input.__len__())]
    matrix[index][remainder] = secu_ops_aux(input, index, remainder, matrix)
    return [matrix[index][remainder], matrix]


def secu_ops_aux(input, index, remainder, matrix):
    if index == -1:
        return False
    elif index == 0 and input[0] == remainder:
        matrix[0][int(remainder)] = True
        return True
    elif matrix[index][remainder] is None:
        result = secu_ops_aux(input, index - 1, remainder - input[index], matrix) or \
                 secu_ops_aux(input, index - 1, remainder / input[index], matrix) or \
                 secu_ops_aux(input, index - 1, remainder ** (1 / input[index]), matrix)
        matrix[index][remainder] = result
        return result


def output_sequence(input, matrix, output):
    n = len(matrix[0]) - 1
    index = len(input) - 1
    if matrix[index][n] == False:
        print("No sequence can create the output of " + str(n))
        return
    for i in range(len(input), 1, -1):
        if matrix[index - 1][n - input[index]]:
            output.append('+')
        elif matrix[index - 1][int(n / input[index])]:
            output.append('/')
        else:
            output.append('^')
    print(output)
    return output


input = [1, 2, 2]
number = 9
seq = []
output_structure = secu_ops(input, input.__len__() - 1, number)
print(output_structure[0])
x = output_sequence(input, output_structure[1], seq)
