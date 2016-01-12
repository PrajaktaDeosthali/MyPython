import urllib.parse
import urllib.request 
import xml.etree.ElementTree as ET

#sample url 
#name = "http://python-data.dr-chuck.net/comments_42.xml"

#actual url 
#name = http://python-data.dr-chuck.net/comments_199362.xml

counter = dict()
userURL = input ("Enter the URL")
print (userURL)
uh = urllib.request.urlopen(userURL)
data = uh.read()
print (len(data))
tree = ET.fromstring(data)

#counts[hr2] = counts.get(hr2,0) +1     
comments = tree.findall('comments/comment/count')
a = type(comments)

 
