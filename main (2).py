'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
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


