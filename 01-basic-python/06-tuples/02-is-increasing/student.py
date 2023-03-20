# Write your code here
def is_increasing(ns):
    uitkomst = True
    ms = ns[1:]
    zipped = list(zip(ns, ms))
    for i in zipped:
        if i[0] > i[1]:
            uitkomst = False
    return uitkomst
