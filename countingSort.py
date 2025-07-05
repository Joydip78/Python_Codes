def countingSort(arr):
    # values are in range 0-99
    count = [0] * 100  
    for num in arr:
        count[num] += 1
    return count

# Read input
n = int(input())
arr = list(map(int, input().strip().split()))

# Process and print
result = countingSort(arr)
print(' '.join(map(str, result)))
