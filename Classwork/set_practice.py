s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 3}
s4 = {1, 2, 3, 4, 5, 6, 7, 8}

s1 |= s2
#print(s1.union(s2))
print(s1.update(s2))
print(s1)
