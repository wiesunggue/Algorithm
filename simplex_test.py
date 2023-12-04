def rref(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    lead = 0  # 주도 원소의 열 인덱스

    for r in range(num_rows):
        if lead >= num_columns:
            break

        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == num_rows:
                i = r
                lead += 1
                if num_columns == lead:
                    break

        # 현재 행과 찾은 행을 교환
        matrix[i], matrix[r] = matrix[r], matrix[i]

        # 현재 행의 주도 원소를 1로 만듦
        pivot = matrix[r][lead]
        matrix[r] = [m / float(pivot) for m in matrix[r]]

        # 다른 행들의 주도 원소를 0으로 만듦
        for i in range(num_rows):
            if i != r:
                factor = matrix[i][lead]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[r])]

        lead += 1

    return matrix

def find_independent_rows(matrix):
    rref_matrix = rref(matrix)
    independent_rows = [row for row in rref_matrix if any(row)]
    return independent_rows

# 1000x1000 크기의 무작위 행렬 생성 (예제용)
import random

example_matrix = [[random.randint(1, 10) for _ in range(1000)] for _ in range(1000)]

independent_rows = find_independent_rows(example_matrix)
print("독립인 행의 수:", len(independent_rows))
