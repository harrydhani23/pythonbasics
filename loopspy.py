
# For loop on a list
int_list = [1,2,3,4,5,6,7,8,9]
for l in int_list:
    print(l)

# For loop on a string
st = "kiddan bai ki bnda"
for c in st:
    print(c)

# For loop on a dictionary
int_dic = {"Harry" : 1, "India" : 2, "Punjab" : 3, "Shivi" : 4.2}
for d in int_dic.items(): #this will return you tuple
    print(d)
for d in int_dic.keys(): #this will return you keys
    print(d)
for d in int_dic.values(): #this will return you values
    print(d)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")
# better way to iterate a dictionary
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

# while loop
a = 5
while a > 0:
    print(a)
    a=a-1

# iterate a list using loop with if condition
def foo(lst):
    return[l for l in lst if not isinstance(l,str) and l>0]
print(foo([1,2,3,4,5,6,7,8,"harrydhani",-1]))

# the loop will go at the end if you add else condition with if condition
def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]
print(foo([1,2,3,4,5,6,7,8,"harrydhani",-1]))


