def pascal_triangle(n):
    triangle = []
    for i in range(n + 1):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle[n]


n = int(input())

for i in range(n):
    print(*pascal_triangle(i))