def check_empty(arr, start_point, end_point):
    for i in range(start_point[0], end_point[0]+1):
        for j in range(start_point[1], end_point[1]+1):
            if arr[i][j]:
                return False
    return True


n = int(input())
yard = [[False for _ in range(n)] for _ in range(n)]
for _ in range(int(input())):
    x, y = tuple(map(lambda x: int(x)-1, input().split()))
    yard[x][y] = True

pool_size = 0
for x, row in enumerate(yard):
    for y, point in enumerate(row):
        while x + pool_size < len(yard) and \
                y + pool_size < len(row) and \
                check_empty(yard, (x, y), (x + pool_size, y + pool_size)):
            pool_size += 1
print(pool_size)
