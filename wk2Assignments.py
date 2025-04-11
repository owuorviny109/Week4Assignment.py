#crating a empty list
my_list=[]

#adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting an element to the list
my_list.insert(1, 15)

#extending the list
my_list1=[50, 60, 70]
my_list.extend(my_list1)

#removing an element from the list
my_list.pop(-1)

#sorting the list in ascending order
my_list.sort()

#find and print the index of an element in the list
print(my_list.index(30))
