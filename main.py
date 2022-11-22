import copy


def la_place(matrix):
    var = copy.deepcopy(matrix)
    if len(var) == 3:
        return var[0][0] * var[1][1] * var[2][2]+var[0][1] * var[1][2] * var[2][0] + var[0][2] * var[1][0] * var[2][1]\
               - var[0][2] * var[1][1] * var[2][0]-var[0][1] * var[1][0] * var[2][2] - var[0][0] * var[1][2] * var[2][1]
    if len(var) == 2:
        return var[0][0] * var[1][1] - var[0][1] * var[1][0]

    g = -1
    det = 0

    for i in range(len(var)):
        g *= -1
        if matrix[0][i] == 0:
            continue
        det += g * matrix[0][i] * la_place(scale_down(var, i))
    return det


def scale_down(matrix, i):
    var = copy.deepcopy(matrix)
    if len(var) > 3:
        var.pop(0)
        for x in range(len(var)):
            var[x].pop(i)
    return var


def check_if_any_Wn_equals_0(arr):
    for n in range(len(arr)):
        if arr[n] == 0:
            return True
    return False


def print_rational_solutions(WnArr):
    for n in range(len(WnArr)):
        print("x" + str(n + 1) + " = " + str(WnArr[n]) + "/" + str(W))


def print_float_solutions(arr):
    for n in range(len(arr)):
        print("x" + str(n + 1) + " = " + str(arr[n]))


def make_Wn_matrix(j, matrix, ys):
    var = copy.deepcopy(matrix)
    for i in range(len(var)):
        var[i][j] = ys[i]
    return var


matrix = []
ys = []
row = []
inp = input("How many variables? >")
for i in range(int(inp)):
    for j in range(int(inp)):
        print("x" + str(j+1),end="")
        row.append(float(input(">")))
    ys.append(float(input("Result of the equation >")))
    print(str(row) + " = " + str(ys[i]))
    matrix.append(row)
    row = []

resultArr = []
WnArr = []

W = la_place(matrix)

for n in range(len(matrix)):
    WnArr.append(la_place((make_Wn_matrix(n, matrix, ys))))

if W == 0:
    if check_if_any_Wn_equals_0(WnArr):
        print("Infinitely many solutions")
        quit()
    else:
        print("No solution")
        quit()

for n in range(len(matrix)):
    resultArr.append(WnArr[n]/W)

print("Solutions as rational fractions:")
print_rational_solutions(WnArr)

print("Solutions as floating point numbers:")
print_float_solutions(resultArr)
