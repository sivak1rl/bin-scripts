#!/usr/bin/python
#add username list /usr/share/seclists/Usernames/top-usernames-shortlist.txt
import socket
import sys
if len(sys.argv) != 2:
	print "Usage: vrfy.py <ip>"
	sys.exit(0)
# Create a Socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the Server
connect=s.connect((sys.argv[1],25))
# Receive the banner
banner=s.recv(1024)
print banner
# VRFY a user
users = ['root', 'admin', 'test', 'guest', 'info', 'adm', 'mysql',\
	 'user', 'administrator', 'oracle', 'ftp', 'pi', 'puppet',\
	 'ansible', 'ec2-user', 'vagrant', 'azureuser' ]
for user in users :
	s.send('VRFY ' + user + '\r\n')
	result=s.recv(1024)
	print result
# Close the socket
s.close()
