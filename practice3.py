n1 = {2, 3, 4, 10}

n2 = {10, 2, 100, 2000}

n3 = n1.union(n2)
print ("n3 is the union\n", n3)

# use the pipe character to do the union operation

n4 = n1 | n2
print ("n4 is the union, too\n", n4)

# now, try intersection of sets

n5 = n1.intersection(n2)
print ("the intersection of sets is \n", n5)

# Use the & character to do the intersection operation

n6 = n1 & n2
print ("useing the & character\n", n6)

# now try Differences in sets

s1 = {'a', 'e','i', 'o', 'u'}
s2 = {'e', 'o'}

s3 = s1.difference(s2)
print ("s1 is  ", s1)
print ("s2 is  ", s2)
print ("s1 - s2 is \n", s3)

s4 = s1 - s2
print ("using the - operator\n", s4)

# now try Symmetric Differences in sets
s1 = {20, 20, 30, 40}
s2 = {30, 40, 200, 300}

s3 = s1.symmetric_difference(s2)
print ("s1  is \n", s1)
print ("s2  is \n", s2)
print ("the symmetric difference is \n", s3)

# use the ^ symbol now

print ("the sym diff using the operator ^ is \n", (s1 ^ s2))

       
