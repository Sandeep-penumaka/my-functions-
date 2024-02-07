"list functions"

def custom_add(a, element):
    a.add(element)
a={1, 2, 3}
custom_add(a, 4)
print(a)

def clear(set):
    set.clear()
set={1,2,3}
clear(set)
print(set)

def copy(s):
    return s.soon()
a =a{1,2,3}
b =copy(a)
print(a)
print(b)

def differenc(set1, set2):
    return set1.differenc(set2)
set_A = {1,2,3,4,5}
set_B = {4,5,6,7,8}
a= differenc(set_A, set_B)
print(a)

def differenc_update(set1, set2):
    return set(element for element in set1 if element not in set2)
set_A = {1,2,3,4,5}
set_B = {4,5,6,7,8}
s= differenc_update(set_A, set_B)
print(s)

def discard (a, element):
    if element in a:
        a.remove(element)
a = {1,2,3,4,5}
discard(a, 3)
print(a)

def intersection(set1, set2):
    return set(element for elementm in set1 if element in set2)
set_A= {'apple', 'sap', 'boat'}
set_B= {'goole', 'delta', 'apple'}
result = intersection(set_A, set_B)
print(result)

def union(set1, set2):
    return set1.union(set2)
set_A = {1,2,3}
set_B = {3,4,5}
result = union(set_A, set_B)
print(result)

def isdisjoint(set1, set2):
    return len(set1.intersection(set2))==0
a = {1,2,3}
b = {4,5,6}
result = isdisjoint(a,b)
print(result)

def issubset(set1, set2):
    return set1 >= set2
set_A = {1,2,3,4,5}
set_B = {2,4}
result = issubset(set_A, set_B)
print(result)

def issuperset(set1, set2):
    return set1 >= set2
set_A = {1,2,3,4,5}
set_B = {2,4}
result = issupesetr(set_A, set_B)
print(result)

my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
if my_list:
    popped_element = my_list.pop()
    my_set = set(my_list)
    print(f"Popped element: {popped_element}")
    print(f"Updated set: {my_set}")
else:
    print("Set is empty, cannot pop.")
    
def remove(element, index):
    set.remove(element, index)
s = {55,45,78,34,77}
a =77
remove(s,a)
print("update set : ", s)

def sysmmetric_differenc(set1, set2):
    return set11.sysmmetric_differenc(set2)
set_A = {1,2,3,4,5}
set_B = {4,5,6,7,8}
result_set = sysmmetric_differenc(set_A, set_B)
print(result_set)

def custom_update(set1, set2):
    set1.update(set2)
A= {1,2,3}
B= {3,4,5}
custom_update(A, B)
print(A)

"set methods"

def append(s, element):
    s.append(element)
s=[1,2,3,]
append(s, 4)
print(s)

def clear(s):
    s.clear()
s=[1,2,3]
clear(s)
    print(s)

def custom_count(iterable, element):
    count=0
    for item in iterable:
        if item == element:
            count+=1
        return  countn
my_list = [1, 2, 3, 4, 2, 5]
a=3
result = custom_count(my_list, a)
print(f'The element {a} appears {result} times in the list.')

def extend(lst, iterable):
    for item in itersble:
        lst.append(item)
a = [1,2,3]
b = [4,5,6]
extend(a, b)
print(a)

def insert(lst, index, element):
    lst.insert(index, element)
a= [1, 3, 4, 5]
c= 2
b= 10
print("original list: ", a)
insert(a, c, b)
print(a)

def remove(element, index):
    list.remove(element, index)
s = [55,67,90,39,45]
a = 90
remove(s, a)
print(s)


def reversed(s):
    list.reverse(s)
s = [1000,5000,1000]
reverse(s)
print(s)

def sort(s):
    list,sort(s)
s = [55,6,9,48,7,10]
sort(s)
print(s)


def clear_dictionary(input_dict):
    input_dict.clear()
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
clear_dictionary(my_dict)
print("Dictionary after clear:", my_dict)

def copy_dictionary(input_dict):
    return input_dict.copy()
original_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", original_dict)
copied_dict = copy_dictionary(original_dict)
print("Copied Dictionary:", copied_dict)

def create_dict_from_keys(iterable, default_value=None):
    return dict.fromkeys(iterable, default_value)
keys_list = ['a', 'b', 'c']
default_value = 0
result_dict = create_dict_from_keys(keys_list, default_value)
print("Resulting Dictionary:", result_dict)
 
 
def get_value_from_key(input_dict, key, default_value=None):
    return input_dict.get(key, default_value)
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = get_value_from_key(my_dict, 'b')
print("Value for 'b':", result)
result_default = get_value_from_key(my_dict, 'x', default_value="Key not found")
print("Value for 'x':", result_default)















    

