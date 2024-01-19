from typing import Dict
import numpy as np
import json
import re
import latex

mat = np.array
vec = np.array


def read_data(filename: str) -> Dict:
    with open(filename, "r") as js:
        data = json.load(js)
    return data

def write_data(filename: str, data: Dict):
    with open(filename, "w") as js:
        json.dump(data, js, indent=4, sort_keys=True)


def gen_matrix() -> mat:
    return np.random.randint(low=0, high=300, size=(8, 6))


def gen_vector(dim: int = 6) -> vec:
    return np.random.randint(low=0, high=300, size=(dim, 1))


def generate_data() -> Dict:
    A = gen_matrix()
    b = gen_vector(8)
    c = gen_vector(6)
    return {"A": A.tolist(),
            "b": b.tolist(),
            "c": c.tolist()}


def get_corner_solution(simplex_table: mat) -> vec:
    return vec([simplex_table[np.argmax(x), -1]
                if 1 == np.count_nonzero(x)
                else 0
                for x in
                simplex_table[:, :simplex_table.shape[1]-1]
                .ravel(order="F")
                .reshape(simplex_table.shape[1]-1, simplex_table.shape[0])
                ]).reshape(simplex_table.shape[1]-1, 1)


def simplex(data: Dict, simplex_table: mat, additive: str = "") -> Dict:
    rows = simplex_table.shape[0]
    columns = simplex_table.shape[1]

    print_data: dict = data.copy()
    print_data["matrices"+additive] = []
    while np.min(simplex_table[0, 0:-1]) < -1e-10:
        matrix_data: dict = {"mat": simplex_table.copy()}
        pivot_column = np.argmin(simplex_table[0, 0:columns-1])
        coef = []
        for i in range(1, rows):
            coef.append(simplex_table[i, -1] /
                        simplex_table[i, pivot_column] if
                        simplex_table[i, pivot_column] != 0
                        else 0)
        coef = [np.inf if x <= 0 else x for x in coef]
        pivot_row = np.argmin(coef) + 1
        pivot_element = simplex_table[pivot_row, pivot_column]
        matrix_data["row"] = pivot_row + 1
        matrix_data["column"] = pivot_column + 1
        matrix_data["elem"] = pivot_element
        print_data["matrices"+additive].append(matrix_data.copy())
        simplex_table[pivot_row, :] /= pivot_element
        for i in range(rows):
            elem = simplex_table[i, pivot_column]
            if i != pivot_row:
                for j in range(columns):
                    simplex_table[i, j] -= elem * simplex_table[pivot_row, j]

    matrix_data: dict = {"mat": simplex_table.copy()}
    matrix_data["column"] = None
    matrix_data["row"] = None
    print_data["matrices"+additive].append(matrix_data.copy())

    amount_of_variables = columns - rows

    optim = vec([simplex_table[np.argmax(x), -1] if
                 1 == np.count_nonzero(x)
                 else 0
                 for x in
                 simplex_table[:, :amount_of_variables]
                 .ravel(order="F")
                 .reshape(amount_of_variables, rows)
                 ]).reshape(amount_of_variables, 1)

    print_data["optim"+additive] = optim
    print_data["obj_function"+additive] = simplex_table[0, -1]

    return print_data


def run():
    mode = input()
    A: mat = mat
    c: vec = vec
    b: vec = vec
    data: dict = {}
    if re.search("[Rr]", mode):
        filename = input()
        data = read_data(filename)
    elif re.search("[Gg]", mode):
        filename = input()
        data = generate_data()
        write_data(filename, data)
    else:
        return

    A = mat(data["A"])
    b = vec(data["b"])
    c = vec(data["c"])
    d = np.concatenate((c.T.tolist()[0], [0 for i in range(8)]))
    d *= -1
    a = np.concatenate((A, np.eye(8)), axis=1)
    simplex_table = np.concatenate(
        (np.reshape(vec(d), (1, len(d))), a), axis=0)

    simplex_table = np.concatenate((simplex_table, np.concatenate(
        ([[0]], b), axis=0)), axis=1)

    data["corner_solution"] = get_corner_solution(simplex_table)
    data = simplex(data, simplex_table)

    simplex_table = np.concatenate((A.T, np.eye(6)*-1, np.eye(6), c), axis=1)
    simplex_table = np.concatenate(
        (np.reshape(vec([0]*14 + [1]*6+[0]), (1, 21)), simplex_table),
        axis=0)

    data["second_simplex_table"] = simplex_table.copy()
    simplex_table[0][:] -= simplex_table[1:].sum(axis=0)
    data["corner_solution_second"] = get_corner_solution(simplex_table)
    data = simplex(data, simplex_table, "_second")

    simplex_table = mat(data["matrices_second"][-1]["mat"])
    simplex_table = np.concatenate((simplex_table[:, :-7],
                                    simplex_table[:, -1].reshape(
                                        (simplex_table.shape[0], 1))
                                    ), axis=1)
    simplex_table[0][:] = 0
    simplex_table[0][:8] = b.T[0, :]

    basis = ([np.argmax(x)
              if 1 == np.count_nonzero(x)
              else -1
              for x in
              simplex_table[1:, :-1]
              .ravel(order="F")
              .reshape(simplex_table.shape[1]-1, simplex_table.shape[0]-1)
              ])

    data["third_simplex_table"] = simplex_table.copy()
    for i, row in enumerate(basis):
        if row != -1 and simplex_table[0, i] != 0:
            simplex_table[0] -= simplex_table[row+1] * simplex_table[0, i]

    data["corner_solution_third"] = get_corner_solution(simplex_table)
    data = simplex(data, simplex_table, "_third")

    latex.preambule(data)


if __name__ == "__main__":
    run()
