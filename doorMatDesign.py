n, m = map(int, input().split())

# Top half of the pattern 
for i in range(1, n, 2):
    pattern = ('.|.' * i).center(m, '-')
    print(pattern)

# Center of the pattern 
print('WELCOME'.center(m, '-'))

# Bottom half
for i in range(n-2, 0, -2):
    pattern = ('.|.' * i).center(m, '-')
    print(pattern)
