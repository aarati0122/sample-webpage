#!/usr/bin/python3
  
import cgi
import subprocess as sp
print("content-type: text/html")
print()

value=cgi.FieldStorage()

command= value.getvalue("x")



#cmd= "sudo {0}".format(command)


output=sp.getoutput(command)
print("Linux Command: {}".format(output))
