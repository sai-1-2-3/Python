#small number in the list
def small_number_loop(list):
    for i in range(len(list)):
        min(list[i:] + list[:i])
    return min(list[i:] + list[:i])

#small number through iteration
def small_number_iter(list):
    least = list[0]
    for i in list:
        if least > i:
            least = i 
    return least 

#using min function without iteration
def small_number_min(list):
    return min(list)

#small number through minimum function
def small_number_min_iter(list):
   #Using minimum function
   '''
   convert to float, int or string
   float(i) for i in list
   int(i) for i in list
   i for i in list
   Using minimum function you don't have to convert
   '''
   return min(i for i in list)

#small_number through sorting
def small_number_sort(list):
    #sort the list using sort()
    list.sort()
    return list[0]


print(small_number_loop(list))
print(small_number_iter(list))
print(small_number_min(list))
print(small_number_min_iter(list))
print(small_number_sort(list))