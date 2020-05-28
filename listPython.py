#===================LIST================

student_names = ['harry', 'inder', 'anuj', 'chandni','bandar','bhangi','ballavana', 10]
print(student_names)

student_rollNumber = [1,2,3,4,5,6,7]
print(student_rollNumber)

student_marks = [70.1, 60.9, 50.3, 45.6, 40.7, 90.1, 99]
print(student_marks)


#==========range To create a List=======
numbers = list(range(1, 10))
print(numbers)

#==========range To create a List Using Third argument Step=======
numbersStep = list(range(1, 10, 2))
print(numbersStep)


#===========multiple list in a list=================

lists = [list(range(1, 10, 2)), list(range(1, 10, 3))]
print(lists)


#===========create a complex list================
complexList = [1,10.2,'kiddan bai',[23,34,56,78]]
print(complexList)


#============list functions======================
num = [2,3,5,6,8,5,3,4,54,4,6,3,4,2,5,3,5,3]
tot = sum(num)
length = len(num)
avg = tot / length
print('max number in the list is -->', max(num))
print('min number in the list is -->', min(num))
print('avg number in the list is -->', avg)
print('count of 2 in num list is -->', num.count(5));

l = [0,2,3,4,2,1]

l.append(5);
print(l)
l.remove(4);
print(l)

# to find the index of the give number
print(l.index(1))     

# to get the item on the given index
print(l.__getitem__(0))
print(l[0])

# to get the items on the given range of index
print(l[1:4])
print(l[:4])
print(l[2:])

# to get the last element of the list
print(l[-1])

# to get the second last element of the list and so on
print(l[-2])



ll = ["harry",0,1,2,3,4,5,[11,22,33,44]]

# get the first character of the first element in the list

print(ll[0])
print(ll[0][0])
print(ll[-1][0])

