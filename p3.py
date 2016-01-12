import urllib.request
import xml.etree.ElementTree as ET

filename = "http://python-data.dr-chuck.net/comments_42.xml"

uh = urllib.request.urlopen(filename)
print (type(uh))
data = uh.read()
print (type (data))

tree = ET.fromstring(data)
print (type(tree))
list1 = list()
count = tree.findall('comments/comment/count')
print (len(count))
a = 0 
for i in count :
  print (int(i.text)) 
  a = a + (int(i.text))
  #print (type(a))
  list1.append(i)

print (count[0].text)
print (type (count))
print ('The count of the new list is')
print (len (list1))
#print (sum(list1))  
print (a)