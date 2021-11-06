#Tuples are same as list but here we use parentheses instead of square brackets. 
# We can accesses the items of a tuple in the same way as list but we cannot change them as they are immutable.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 300 will result in an error
#looping over a tuple
for dimension in dimensions:
    print(dimension)
#Writing over a tuple: We will have to reassign the entire tuple
dimensions = (400, 50)
for dimension in dimensions:
    print(dimension)
#PEP Python Enhancement Proposal
