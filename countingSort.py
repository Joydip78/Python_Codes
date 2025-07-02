def countingSort(arr):
    count = [0] * 100  # values are in range 0-99
    for num in arr:
        count[num] += 1
    return count

# Read input
n = int(input())
arr = list(map(int, input().strip().split()))

# Process and print
result = countingSort(arr)
print(' '.join(map(str, result)))
