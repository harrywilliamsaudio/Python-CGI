#!/usr/bin/python3 
#Author : Harry Williams
#My first CGI Python script 

import cgi,cgitb,os,re,sys,codecs,urllib.request
sys.stdout = codecs.getwriter ("utf -8")(sys.stdout.detach ())
cgitb.enable()
print ('''\
Content-type: text/html
<!DOCTYPE html>
<html lang ='en-GB'>
<head>
<meta charset ="utf-8">
<title> CGI Python Script </title>
</head>
<body>''')
print ('''<section>\n<h1> Environment Variables </h1>''')
print ('''<table>\n<tbody>''')
for k in sorted (os.environ.keys()):
	print ("<tr><th>" + k + "</th><td> " + os.environ[k] +
	"</td></tr>")
print ('''</tbody>\n</table>\n<p></p>\n</section>''')
# Code for Exercise 1g here
print (''' </body>\n</html>''')
