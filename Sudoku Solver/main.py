def my_copy(self):
    list = [[0 for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            list[i][j] = self[i][j].copy()
    return list


def MRV(valid_values):
    min = 1000
    x = 10
    y = 10
    for i in range(9):
        for j in range(9):
            length = len(valid_values[i][j])
            if (length < min) and length != 1:
                min = length
                x = i
                y = j
    return x, y


def backtracking(valid_values):
    var_index = MRV(valid_values)
    if var_index[0] == 10:
        return valid_values
    values = valid_values[var_index[0]][var_index[1]]
    for value in values:
        valid_values_copy = my_copy(valid_values)
        valid_values_copy[var_index[0]][var_index[1]] = [value]
        ans = AC_3(get_neighbors(var_index[0], var_index[1]), valid_values_copy)
        if ans:
            result = backtracking(valid_values_copy)
            if result != "failure":
                return result
    return "failure"


def AC_3(queue, valid_values):
    while len(queue) != 0:
        arc = queue.pop(0)
        source = arc[0]
        destination = arc[1]
        if len(valid_values[destination[0]][destination[1]]) == 1:
            value = valid_values[destination[0]][destination[1]][0]
            if value in valid_values[source[0]][source[1]]:
                valid_values[source[0]][source[1]].remove(value)
                length = len(valid_values[source[0]][source[1]])
                if length == 1:
                    queue += get_neighbors(source[0], source[1])
                elif length == 0:
                    return False
    return True


def get_neighbors(i, j):
    neighbors = []
    for k in range(9):
        if k != j:
            neighbors.append([[i, k], [i, j]])
        if k != i:
            neighbors.append([[k, j], [i, j]])
    y = i // 3
    x = j // 3
    for k in range(3):
        for h in range(3):
            if y * 3 + k != i and x * 3 + h != j:
                neighbors.append([[y * 3 + k, x * 3 + h], [i, j]])
    return neighbors


def print_table(table):
    for i in range(9):
        for j in range(9):
            print(table[i][j][0], end=' ')
        print()


valid_values = [[[k + 1 for k in range(9)] for j in range(9)] for i in range(9)]
for i in range(9):
    row = input().split()
    for j in range(9):
        if row[j] != '.':
            num = int(row[j])
            valid_values[i][j] = [num]
            AC_3(get_neighbors(i, j), valid_values)
print_table(backtracking(valid_values))
