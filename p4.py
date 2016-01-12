import urllib.request
import xml.etree.ElementTree as ET

filename = "http://python-data.dr-chuck.net/comments_199362.xml"

uh = urllib.request.urlopen(filename)
data = uh.read()


tree = ET.fromstring(data)
count = tree.findall('comments/comment/count')
a = 0 
for i in count :
  a = a + (int(i.text))


print (len (count))
  
print (a)