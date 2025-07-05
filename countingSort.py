def countingSort(arr):
    # values are in range 0-99
    count = [0] * 100  
    for num in arr:
        count[num] += 1
    return count

n = int(input()) # Read input
arr = list(map(int, input().strip().split()))


result = countingSort(arr) # Process and print
print(' '.join(map(str, result)))
