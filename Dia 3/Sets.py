mi_set = set([1,2,3,4,5])
print(type(mi_set))
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s3.add(6)
s3.add(2)
print(s3)