def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

primes = [1, 3, 5, 7, 9]

print binary_search(primes, 9)
