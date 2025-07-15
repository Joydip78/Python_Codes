def countingSort(arr):
    
    count = [0] * 100  # values are in range 0-99
    for num in arr:
        count[num] += 1
    return count

n = int(input()) # Read input
arr = list(map(int, input().strip().split()))


result = countingSort(arr) # Process and store
print(' '.join(map(str, result)))
