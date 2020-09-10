#Sorting


array = input()

array_list = list()
for i in array:
    array_list.append(int(i))

array_list.sort(reverse= True)

for i in array_list:
    print(i, end='')