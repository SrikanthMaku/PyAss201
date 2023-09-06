# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

tuple = [(2,5),(1,2),(4,4),(2,3,),(2,1)]

def sort(tuple):
    tuple.sort(key = lambda a: a[-1])
    return tuple

print("sorted tuple list:",sort(tuple))






