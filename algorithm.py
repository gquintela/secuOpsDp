
def secu_ops(input, remainder):
    """
    Given an array of numbers, and a target value, verifies if the target value can be reached computing from left
    to right using addition, multiplication or potenciation.
    :param input: array of numbers
    :param remainder: target value
    :return: list[answer: boolean ,memoization structure]
    """
    index = input.__len__() - 1
    matrix = [[None for i in range(0, remainder + 1)]
              for j in range(0, input.__len__())]
    matrix[index][remainder] = secu_ops_aux(input, index, remainder, matrix)
    return [matrix[index][remainder], matrix]

def secu_ops_aux(input, index, remainder, matrix):
    """
    Auxiliar method called in order to recurse called initially by secu_ops
    :param input: array of numbers
    :param index: actual index in array
    :param remainder: target value
    :param matrix: memoization structure
    :return: memoization structure
    """
    if index == -1 or remainder < 0:
        return False
    elif index == 0 and input[0] == remainder:
        matrix[0][int(remainder)] = True
        return True
    elif matrix[index][remainder] is None:
        add = secu_ops_aux(input, index - 1, remainder - input[index], matrix)
        if remainder % input[index] == 0:
            product = secu_ops_aux(input, index - 1, int(remainder / input[index]), matrix)
        else:
            product = False
        nroot =remainder ** (1 / input[index])
        if remainder > 0 and nroot.is_integer():
            exponentiation = secu_ops_aux(input, index - 1, int(nroot), matrix)
        else:
            exponentiation = False
        result =  exponentiation or add or product
        matrix[index][remainder] = result
        return result
    else:
        return matrix[index][remainder]

def print_sequence(input, matrix, number):
    """
    takes the boolean matrix and recreates the solution if exists.
    @:param input secuence of numbers
    @:param matrix boolean matrix of (number+1)*input.size
    @:param number the targeted number
    """
    output = []
    n = len(matrix[0]) - 1
    index = len(input) - 1
    if matrix[index][n] == False:
        print("No sequence of the numbers ", end='')
        for n in input:
            print(n,end=' ')
        print("can create the output of " + str(n))
        print("   using adition, multiplication or exponenciation.")
        return []
    for i in range(len(input), 1, -1):
        if matrix[index - 1][n - input[index]]:
            output.insert(0,'+')
            n = n - input[index]
        elif n % input[index] == 0 and matrix[index - 1][int(n / input[index])]:
            output.insert(0,'*')
            n = int(n / input[index])
        elif (n ** (1 / input[index])).is_integer():
            output.insert(0,'^')
            n = int(n ** (1 / input[index]))
        index -= 1
    if(len(input) == 0):
        print ([])
    elif (len(input) == 1):
        print (input[0])
    else:
        print(str(number) +" can be created the following way")
        [print('(', end='') for i in range(0,len(input)-1)]
        print(str(input[0]),end='')
        for i in range(0, len(output)):
            print(output[i],end='')
            print(str(input[i + 1]) + ')',end='')
    return output