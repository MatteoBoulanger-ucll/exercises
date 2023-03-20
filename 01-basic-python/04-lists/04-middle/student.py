# Write your code here
def middle(lijst):
    a = len(lijst)
    if a % 2 == 0:
        return lijst[a//2-1:a//2+1]
    else:
        return lijst[a//2]
