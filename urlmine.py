# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import socket 
import urllib
from BeautifulSoup import *

# file to be retrived http://www.pythonlearn.com/code/intro-short.txt
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

#url = 'http://dr-chuck.com/'
#html = urllib.urlopen(url).read()


data = mysock.recv(512)
soup = BeautifulSoup(data)
print (soup)

mysock.close()