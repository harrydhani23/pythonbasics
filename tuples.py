t = (1,2,3,4) 
l = [1,2,3,4]

#==== list is mutable i.e we can remove data and add data to list====
l.append(5);
print(l)
l.remove(4);
print(l)

#==== whereas, tuples are immutable i.e we cannot add or remove data from tuples once created====
t.append(5)
print(t)