# Write your code here
def add_indices(lijst):
    indices = []
    elementen = len(lijst)
    for i in range(elementen):
        indices.append(i)
    return list(zip(indices, lijst))
