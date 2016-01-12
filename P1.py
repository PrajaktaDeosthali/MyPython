import re

line = "Why should you learn to write programs? 7746 12 1929 8827"
list1 = list()
num = 0 
list1 = re.findall('[0-9]+\S', line)
for l in list1 :
    num = num + int(l) 
print (list1)
print (num)

list2 = list()
num1 = 0 
name = "regex_sum_199360.txt"
handle = open(name)
h = handle.read()
list2 = re.findall('[0-9]+\S', h)
for l in list2 :
    num1 = num1 + int(l) 
print (num1)





