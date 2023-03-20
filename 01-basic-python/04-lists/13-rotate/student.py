# Write your code here
def rotates(xs, n):
    return xs[n:] + xs[:n]


print(rotates([1, 2, 3], 2))
