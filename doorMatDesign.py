n, m = map(int, input().split())

# Top half
for i in range(1, n, 2):
    pattern = ('.|.' * i).center(m, '-')
    print(pattern)

# Center
print('WELCOME'.center(m, '-'))

# Bottom half
for i in range(n-2, 0, -2):
    pattern = ('.|.' * i).center(m, '-')
    print(pattern)
