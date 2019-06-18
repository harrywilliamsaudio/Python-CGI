#!/usr/bin/python3
# Import modules for CGI handling 
import cgi, cgitb 
print ("Content-type:text/html\r\n\r\n")
print ("<html lang = 'en-GB'>")
print ("<head>")
print ("<title>Word Analyser</title>")
print ("</head>")
print ("<body>")



print('''<link rel="stylesheet" href="/static/style.css" type="text/css">''')

print('''<form action="words.py" method="POST">''')
print('''<h1>Document Analyser</h1>''')
print('''</div>''')
 
print('''<div class="login-form">''')
print('''<div class="control-group">''')
print('''<input type="text" class="login-field" value="" placeholder="Input File URL" name="input_file1">''')
print('''<label class="login-field-icon fui-user" for="login-name"></label>''')
print('''</div>''')
print('''<h4>OR</h4>''')
print('''<div class="control-group">''')
print('''<textarea rows="5" cols="32" class="login-field" value="" placeholder="Enter Text to Analyse" name="input_file2"></textarea>''')
print('''<label class="login-field-icon fui-lock" for="login-pass"></label>''')
print('''</div>''')
 
print('''<input type="submit" value="Analyse" class="btn btn-primary btn-large btn-block" >''')
print('''<br>''')
print('''</div>''')
print('''</div>''')
print('''</div>''')
print('''</form>''')

print('''</body>''')