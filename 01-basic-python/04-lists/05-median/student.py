# Write your code here

lijst = [1, 5, 3, 2, 4, 9]

lijst.sort()

aantal_elementen = len(lijst)

if aantal_elementen % 2 != 0:
    print(lijst[aantal_elementen//2])
else:
    print(lijst[aantal_elementen//2:aantal_elementen//2-1])
